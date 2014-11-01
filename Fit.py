import ROOT, multiprocessing

masses = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
#masses = [125]
combination = False
if combination:
    #masses = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
    masses = [125]

#############################################################
def runAsymptoticsCLs(datatype = 'asimovData'):
    """
    Calculate limits on the workspace
    """

    ROOT.gSystem.Load('scripts/runAsymptoticsCLs_C.so')

    processes = []

    ## Create one process for each mass point
    for mass in masses:

        if not combination:
            name = 'VHhh_%d' % mass
            workspace_file = './results/MEAS_combined_%s_model.root' % name
        if combination:
            name = 'VH_%d' % mass
            workspace_file = './combination/MEAS_combined_%s_model.root' % name


        ## create the process to derive the limit for this mass
        p = multiprocessing.Process(target=ROOT.runAsymptoticsCLs, args=(workspace_file,
                                                                         'combined',
                                                                         'ModelConfig',
                                                                         datatype,
                                                                         'asimovData_0',
                                                                         #'conditionalGlobs_0',
                                                                         #'nominalGlobs',
                                                                         name,
                                                                         str(mass),
                                                                         0.95))

        processes.append(p)

    ## Execute the processes
    for p in processes:
        p.start()


    ## Wait for all the processes to finish before proceeding to the rest of the code
    for p in processes:
        p.join()


    ## Retrieve the limits from the root file that the script dumps, and display
    for mass in masses:
        name = 'VHhh_%d' % mass
        if combination:
            name = 'VH_%d' % mass
        limits_file = ROOT.TFile('./root-files/%s/%d.root' % (name, mass))
        limits_histogram = limits_file.Get('limit')
        
        observed = limits_histogram.GetBinContent(1)
        median   = limits_histogram.GetBinContent(2)
        sigma_plus_2 = limits_histogram.GetBinContent(3)
        sigma_plus_1 = limits_histogram.GetBinContent(4)
        sigma_minus_1 = limits_histogram.GetBinContent(5)
        sigma_minus_2 = limits_histogram.GetBinContent(6)

        print '============================='
        print 'For %d GeV signal hypothesis:' % mass
        print '-----------------------------'
        #print 'Observed limit : %.2f x SM Higgs production cross-section' % observed
        print 'Expected limit : %.2f x SM Higgs production cross-section' % median
        print 'Expected limit +2sigma : %.2f' % sigma_plus_2
        print 'Expected limit +1sigma : %.2f' % sigma_plus_1
        print 'Expected limit -1sigma : %.2f' % sigma_minus_1
        print 'Expected limit -2sigma : %.2f' % sigma_minus_2


################################################################

#############################################################
def runSig(datatype = 'asimovData'):
    """
    Calculate limits on the workspace
    """

    ROOT.gSystem.Load('scripts/runSig_C.so')

    processes = []

    ## Create one process for each mass point
    for mass in masses:

        name = 'VHhh_%d' % mass
        workspace_file = './results/MEAS_combined_%s_model.root' % name
        if combination:
            name = 'VH_%d' % mass
            workspace_file = './combination/MEAS_combined_%s_model.root' % name

        ## create the process to derive the limit for this mass
        p = multiprocessing.Process(target=ROOT.runSig, args=(workspace_file,
                                                              'combined',
                                                              'ModelConfig',
                                                              datatype,
                                                              'asimovData_1',
                                                              'conditionalGlobs_1',
                                                              'nominalGlobs',
                                                              str(mass),
                                                              name))

        processes.append(p)

    ## Execute the processes
    for p in processes:
        p.start()


    ## Wait for all the processes to finish before proceeding to the rest of the code
    for p in processes:
        p.join()


    ## Retrieve the limits from the root file that the script dumps, and display
    for mass in masses:
        name = 'VHhh_%d' % mass
        if combination:
            name = 'VH_%d' % mass
        sig_file = ROOT.TFile('./root-files/%s/P0_MEAS_combined_%s_model.root.root' % (name, name))
        sig_histogram = sig_file.Get('hypo')
        
        obs = sig_histogram.GetBinContent(1)
        sig = sig_histogram.GetBinContent(2)
        #sigs['%s_%d' % (name, mass)] = (sig, obs)

        print '============================='
        print 'For %d GeV signal hypothesis:' % mass
        print '-----------------------------'
        print 'Observed significance : %.2f' % obs
        print 'Expected significance : %.2f' % sig


################################################################
## Main programs
runAsymptoticsCLs()
#runSig()
