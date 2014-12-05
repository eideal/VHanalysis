import os, pickle, shutil
#import ROOT
from Tools.Systematics.sys_classes import SysSet


f = open('Tools/Systematics/EmmaSys.sys', 'rb')
sys_set = pickle.load(f)

shutil.copyfile('workspaceAllMC.root', 'workspaceAllMC_pruned.root')

sys_set.open_files('workspaceAllMC_pruned.root', ['wh','zh'])
sys_set.reset()
        
## STEP 1 : Quadrature combinations
sys_set.quadrature_combination()

## STEP 2 : Symetrization
#sys_set.symmetrize()

## STEP 3 : Kolmogorov-Smirnov pruning
sys_set.prune()

## STEP 4 : Smoothing
#self.sys_set.smooth()

## STEP 5 : Partial symmetrization
#self.sys_set.partial_symmetrize()

## STEP 6 : Normalize shape variations to nominal
sys_set.norm_to_overall()

## STEP 7 : Significance pruning
#self.sys_set.prune_significance()

## STEP 8 : 10% on Shapes
sys_set.prune_shape_10()

## STEP 9 : 0.5% Thresholds
sys_set.prune_05_percent()


f = open('%s.sys' % sys_set.name, 'wb')
pickle.dump(sys_set, f)
f.close()
