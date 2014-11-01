from Sample import Sample 


############## The samples below were from a CN run that I did to get all the signal samples with the truth Higgs pT in there, so I could do an inclusive WH and inclusive ZH comparison from D3PD to CN
WH125_tautauhh = Sample(
    name = 'WH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedWHhh/WH_hh/WH125_tautauhh.root')

WH125_tautaulh = Sample(
    name = 'WH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedWHlh/WH_lh/WH125_tautaulh.root')
ZH125_tautauhh = Sample(
    name = 'ZH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedZHhh/ZH_hh/ZH125_tautauhh.root')

ZH125_tautaulh = Sample(
    name = 'ZH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedZHlh/ZH_lh/ZH125_tautaulh.root')

#ZH125_tautaull = Sample(
#    name = 'ZH125_tautaull',
#    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedZHll/ZH_ll/ZH125_tautaull.root')

#WH125_tautaull = Sample(
#    name = 'WH125_tautaull',
#    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-04Test_Emma/MergedWHll/WH_ll/WH125_tautaull.root')
#


########### The samples below here are for looking at the effect of the CN to D3PD reweighting that I've put into the CN: 
WH125_tautauhh_Up = Sample(
    name = 'WH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedWHhh/WH_hh/WH125_tautauhh.root')

WH125_tautaulh_Up = Sample(
    name = 'WH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedWHlh/WH_lh/WH125_tautaulh.root')

ZH125_tautauhh_Up = Sample(            
    name = 'ZH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedZHhh/ZH_hh/ZH125_tautauhh.root')

ZH125_tautaulh_Up = Sample(
    name = 'ZH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedZHlh/ZH_lh/ZH125_tautaulh.root')

WH125_tautauhh_Down = Sample(
    name = 'WH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedWHhh/WH_hh/WH125_tautauhh.root')

WH125_tautaulh_Down = Sample(
    name = 'WH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedWHlh/WH_lh/WH125_tautaulh.root')

ZH125_tautauhh_Down = Sample(            
    name = 'ZH125_tautauhh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedZHhh/ZH_hh/ZH125_tautauhh.root')

ZH125_tautaulh_Down = Sample(
    name = 'ZH125_tautaulh',
    path = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv01-07Test_Emma/MergedZHlh/ZH_lh/ZH125_tautaulh.root')