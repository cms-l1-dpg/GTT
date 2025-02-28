import argparse
import ROOT
import math
ROOT.gROOT.SetBatch(True) #Do not display any graphics

parser = argparse.ArgumentParser(description='Analyses L1TrackNtuples and produces some performance plots')
parser.add_argument('--i',help='Input Filename',required=True)
parser.add_argument('--o',help='Output Filename',required=True)
args = parser.parse_args()

input_files = args.i
output_file = args.o

print ("Reading Input: ",input_files)
print ("Saving Output: ",output_file)

#GEN:
genPt=ROOT.TH1D("genPt","genPt",100,0.0,100.0)
genPhi=ROOT.TH1D("genPhi","genPhi",80,-4.0,4.0)
genPID=ROOT.TH1D("genPID","genPID",1000,-500.0,500.0)

#Tracks:
trackPt=ROOT.TH1D("trackPt","trackPt",100,0.0,100.0)
trackEta=ROOT.TH1D("trackEta","trackEta",100,-5.0,5.0)
trackPhi=ROOT.TH1D("trackPhi","trackPhi",80,-4.0,4.0)
trackChi2=ROOT.TH1D("trackChi2","trackChi2",100,0.0,100.0)
trackMVA=ROOT.TH1D("trackMVA","trackMVA",100,0.0,1.0)
trackFake=ROOT.TH1D("trackFake","trackFake",3,0.0,3.0)
trackz0=ROOT.TH1D("trackz0","trackz0",60,-30.0,30.0)

# trackExtPt=ROOT.TH1D("trackExtPt","trackExtPt",100,0.0,100.0)
# trackExtEta=ROOT.TH1D("trackExtEta","trackExtEta",100,-5.0,5.0)
# trackExtPhi=ROOT.TH1D("trackExtPhi","trackExtPhi",80,-4.0,4.0)
# trackExtChi2=ROOT.TH1D("trackExtChi2","trackExtChi2",100,0.0,100.0)
# trackExtMVA=ROOT.TH1D("trackExtMVA","trackExtMVA",100,0.0,1.0)
# trackExtFake=ROOT.TH1D("trackExtFake","trackExtFake",3,0.0,3.0)
# trackExtD0=ROOT.TH1D("trackExtD0","trackExtD0",100,0.0,100.0)

#Primary Vertex:
pvReco=ROOT.TH1D("pvReco","pvReco",256,-20.0,20.0)
pvMC=ROOT.TH1D("pvMC","pvMC",256,-20.0,20.0)
pvRes=ROOT.TH1D("pvRes","pvRes",1024,-20.0,20.0)
pvResEmu=ROOT.TH1D("pvResEmu","pvResEmu",1024,-20.0,20.0)

#Jets:
genJetPt=ROOT.TH1D("genJetPt","genJetPt",1000,0.0,1000.0)
genJetPtB=ROOT.TH1D("genJetPtB","genJetPtB",1000,0.0,1000.0)
genJetPtE=ROOT.TH1D("genJetPtE","genJetPtE",1000,0.0,1000.0)
genJetPassedPt=ROOT.TH1D("genJetPassedPt","genJetPassedPt",1000,0.0,1000.0)
genJetPassedPtB=ROOT.TH1D("genJetPassedPtB","genJetPassedPtB",1000,0.0,1000.0)
genJetPassedPtE=ROOT.TH1D("genJetPassedPtE","genJetPassedPtE",1000,0.0,1000.0)
genJetPassedEmuPt=ROOT.TH1D("genJetPassedEmuPt","genJetPassedEmuPt",1000,0.0,1000.0)
genJetPassedEmuPtB=ROOT.TH1D("genJetPassedEmuPtB","genJetPassedEmuPtB",1000,0.0,1000.0)
genJetPassedEmuPtE=ROOT.TH1D("genJetPassedEmuPtE","genJetPassedEmuPtE",1000,0.0,1000.0)
tkJetPt=ROOT.TH1D("tkJetPt","tkJetPt",1000,0.0,1000.0)
tkJetEmuPt=ROOT.TH1D("tkJetEmuPt","tkJetEmuPt",1000,0.0,1000.0)
tkJetPtvsGenPt=ROOT.TH2D("tkJetPtvsGenPt","tkJetPtvsGenPt",1000,0.0,1000.0,1000,0.0,1000.0)
tkJetEmuPtvsGenPt=ROOT.TH2D("tkJetEmuPtvsGenPt","tkJetEmuPtvsGenPt",1000,0.0,1000.0,1000,0.0,1000.0)
tkJetPull=ROOT.TH1D("tkJetPull","tkJetPull",500,-250.0,250.0)
tkJetEmuPull=ROOT.TH1D("tkJetEmuPull","tkJetEmuPull",500,-250.0,250.0)

#MET:
tpEta=ROOT.TH1D("tpEta","tpEta",100,-5.0,5.0)
tpPt=ROOT.TH1D("tpPt","tpPt",1000,0.0,1000.0)
tpMatchedEta=ROOT.TH1D("tpMatchedEta","tpMatchedEta",100,-5.0,5.0)
tpMatchedPt=ROOT.TH1D("tpMatchedPt","tpMatchedPt",1000,0.0,1000.0)
denMET=ROOT.TH1D("denMET","denMET",1000,0.0,1000.0)
numMET=ROOT.TH1D("numMET","numMET",1000,0.0,1000.0)
METRes=ROOT.TH1D("METRes","METRes",1000,-2.0,48.0)

outputFile = ROOT.TFile(output_file,'RECREATE')

file = ROOT.TFile(input_files,'read')
tree = file.Get("L1TrackNtuple/eventTree")
# tree.Print()

chatty = False
# chatty = True

# dRCut=0.1
dRCut=0.4
counter=0
goodVtx=0
JetThreshold=50.0 #Define as passed if the TkJet is above this threshold

### Go through events in the tree and loop over vectors of tracks to fill plots: ###
for event in tree:
    # if counter>20: break
    if (chatty): print("\nEvent[{0}]".format(counter))

    ### Gen Info ###
    for gpt in event.gen_pt: genPt.Fill(gpt)
    for gphi in event.gen_phi: genPhi.Fill(gphi)
    for gpid in event.gen_pdgid: genPID.Fill(gpid)

    ### Tracks ###
    for pt in event.trk_pt: trackPt.Fill(pt)
    for eta in event.trk_eta: trackEta.Fill(eta)
    for phi in event.trk_phi: trackPhi.Fill(phi)
    for chi2 in event.trk_chi2: trackChi2.Fill(chi2)
    for mva in event.trk_MVA1: trackMVA.Fill(mva)
    for trkFake in event.trk_fake: trackFake.Fill(trkFake)
    for trkz0 in event.trk_z0: trackz0.Fill(trkz0)

    # for pt in event.trkExt_pt: trackExtPt.Fill(pt)
    # for eta in event.trkExt_eta: trackExtEta.Fill(eta)
    # for phi in event.trkExt_phi: trackExtPhi.Fill(phi)
    # for chi2 in event.trkExt_chi2: trackExtChi2.Fill(chi2)
    # for mva in event.trkExt_MVA: trackExtMVA.Fill(mva)
    # for d0 in event.trkExt_d0: trackExtMVA.Fill(d0)
    # for trkFake in event.trkExt_fake: trackExtFake.Fill(trkFake)

    ### Primary Vertex ###
    pvMC.Fill(event.pv_MC[0])
    pvReco.Fill(event.pv_L1reco[0])
    pvRes.Fill(event.pv_MC[0]-event.pv_L1reco[0])
    pvResEmu.Fill(event.pv_MC[0]-event.pv_L1reco_emu[0]) #in CMSSW12
    # if (chatty):
    #     print ("event.pv_MC: ", event.pv_MC[0]),
    #     print ("event.pv_MC: ", event.pv_MC[0]),
    #     print ("\tevent.pv_L1reco: ", event.pv_L1reco[0]),
    #     print ("\tres(MC-Reco): ", event.pv_MC[0]-event.pv_L1reco[0]),
    #     print ("\tres(MC-Emu): ", event.pv_MC[0]-event.pv_L1reco_emu[0])
    if (abs(event.pv_MC[0]-event.pv_L1reco_emu[0])>10): print (str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event()))
    if (abs(event.pv_MC[0]-event.pv_L1reco_emu[0])<0.5): goodVtx+=1 # i.e. within 1 cm of gen PV

    ### MET ###
    if (chatty): print("trueMET: "+str(event.trueMET)+" trueTkMET: "+str(event.trueTkMET))

    # True MET
    trueMETx=trueMETy=0
    for i,gen in enumerate(event.gen_pdgid):
        if abs(gen) == (12 or 14 or 16 or 1000022): #neutrino or SUSY stop
            if (chatty): print("["+str(i)+"] gen: "+str(gen))
            trueMETx += event.gen_pt[i] * math.cos(event.gen_phi[i])
            trueMETy += event.gen_pt[i] * math.sin(event.gen_phi[i])
    if (chatty): print("From Neutrinos/BSM trueMETx: "+str(trueMETx)+" trueMETy: "+str(trueMETy)+" myTrueMET: "+ str(math.sqrt(trueMETx*trueMETx + trueMETy*trueMETy)))
 
    # True TkMET
    tpTrueTkMETx=tpTrueTkMETy=0
    tpTrueTkMET=0
    for i,tp in enumerate(event.tp_pt):
        if event.tp_eventid[i]!=0: continue
        if (event.tp_charge[i]==0 or abs(event.tp_eta[i])>2.4 or event.tp_pt[i]<2.0 or event.tp_nstub[i]<4 or abs(event.tp_z0[i])>15): continue
        # print("["+str(i)+"] tp_eventid: "+str(event.tp_eventid[i]))
        tpTrueTkMETx += event.tp_pt[i] * math.cos(event.tp_phi[i]);
        tpTrueTkMETy += event.tp_pt[i] * math.sin(event.tp_phi[i]);
        tpTrueTkMET=math.sqrt(tpTrueTkMETx*tpTrueTkMETx + tpTrueTkMETy*tpTrueTkMETy)

        #Eff Denominator
        tpPt.Fill(event.tp_pt[i])
        tpEta.Fill(event.tp_eta[i])

        if (event.tp_nmatch[i]<1): continue
        if (event.matchtrk_pt[i]<0.0): continue

        #Eff Numerator
        tpMatchedPt.Fill(event.tp_pt[i])
        tpMatchedEta.Fill(event.tp_eta[i])
    if (chatty): print("trueTkMETx: {1} trueTkMETy: {2} myTrueTkMET: {3}".format(tpTrueTkMETx, tpTrueTkMETy, tpTrueTkMET))

    # TkMET
    denMET.Fill(event.trueMET)
    if (event.trkMETEmu>100.0): numMET.Fill(event.trueMET)

    # TkMET Resolutions
    # if (event.trueTkMET>0):
    #     METRes.Fill((event.trkMETEmu-event.trueTkMET)/event.trueTkMET)
    #     if (chatty): print("trueTkMET: {1} trkMETEmu: {2} Res: {3}".format(event.trueTkMET, event.trkMETEmu, ((event.trkMETEmu-event.trueTkMET)/event.trueTkMET)))
    # else: print("trueTkMET: {0} trkMETEmu: {1}".format(event.trueTkMET, event.trkMETEmu))
    ## Using TP calculation:
    if (tpTrueTkMET>0):
        METRes.Fill((event.trkMETEmu-tpTrueTkMET)/tpTrueTkMET)
        if (chatty): print("trueTkMET: {1} trkMETEmu: {2} Res: {3}".format(tpTrueTkMET, event.trkMETEmu, ((event.trkMETEmu-tpTrueTkMET)/tpTrueTkMET)))
    else: print("trueTkMET: {0} trkMETEmu: {1}".format(tpTrueTkMET, event.trkMETEmu))


    ### Jets ###
    for nTkJet,teta in enumerate(event.trkjet_eta):
        if (chatty): print("TkJet[{0}]\teta:{1}\tpT:{2}".format(nTkJet,teta,event.trkjet_pt[nTkJet]))
        tkJetPt.Fill(event.trkjet_pt[nTkJet])
    for nTkEmuJet,tEeta in enumerate(event.trkjetem_eta):
        if (chatty): print("TkEmuJet[{0}]\teta:{1}\tpT:{2}".format(nTkEmuJet,tEeta,event.trkjetem_pt[nTkEmuJet]))
        tkJetEmuPt.Fill(event.trkjetem_pt[nTkEmuJet])

    # Loop over the genJets:
    for nGenJet,geta in enumerate(event.genjet_eta):
        if (abs(geta)>2.4): continue
        # if (event.genjet_pt[nGenJet]<30.0): continue
        genJetPt.Fill(event.genjet_pt[nGenJet])
        if (chatty): print("GenJet[{0}]\teta:{1}\tpT:{2}".format(nGenJet,geta,event.genjet_pt[nGenJet]))
        foundGenEmuJet = False
        foundGenEmuJetB = False
        foundGenEmuJetE = False
        foundGenJet = False
        foundGenJetB = False
        foundGenJetE = False
        MaxTkEmuJetPt=0
        MaxTkJetPt=0
        if (abs(geta)<1.5): genJetPtB.Fill(event.genjet_pt[nGenJet])
        else: genJetPtE.Fill(event.genjet_pt[nGenJet])

        #Loop over Emulated TkJets and match to the genJet:
        for nTkEmuJet,tEeta in enumerate(event.trkjetem_eta):
            TkEmuJetPt=event.trkjetem_pt[nTkEmuJet]
            # if (abs(geta-tEeta)<dRCut and abs(tEeta)<2.4):
            if (abs(geta-tEeta)<dRCut and abs(tEeta)<2.4 and TkEmuJetPt>JetThreshold):
                if (chatty): print("\tabs(geta-tEeta):{0}\tTkEmuJet[{1}] eta:{2}\tphi:{2}\tpT:{3}".format(abs(geta-tEeta),nTkEmuJet,tEeta,event.trkjetem_phi[nTkEmuJet],TkEmuJetPt))
                foundGenEmuJet = True
                if (TkEmuJetPt>MaxTkEmuJetPt): MaxTkEmuJetPt=TkEmuJetPt
                # tkJetEmuPtvsGenPt.Fill(event.genjet_pt[nGenJet],TkEmuJetPt)
                if (abs(geta)<1.5): foundGenEmuJetB = True
                else: foundGenEmuJetE = True
        if (foundGenEmuJet):
            tkJetEmuPtvsGenPt.Fill(event.genjet_pt[nGenJet],MaxTkEmuJetPt) # 2D histogram
            tkJetEmuPull.Fill(event.genjet_pt[nGenJet]-MaxTkEmuJetPt)

        #Loop over Simulated TkJets and match to the genJet:
        for nTkJet,teta in enumerate(event.trkjet_eta):
            TkJetPt=event.trkjet_pt[nTkJet]
            # if (abs(geta-teta)<dRCut and abs(teta)<2.4):
            if (abs(geta-teta)<dRCut and abs(teta)<2.4 and TkJetPt>JetThreshold):
                if (chatty): print("\tabs(geta-teta):{0}\tTkJet[{1}] eta:{2}\tphi:{2}\tpT:{3}".format(abs(geta-teta),nTkJet,teta,event.trkjet_phi[nTkJet],TkJetPt))
                foundGenJet = True
                if (TkJetPt>MaxTkJetPt):  MaxTkJetPt=TkJetPt
                # tkJetPtvsGenPt.Fill(event.genjet_pt[nGenJet],TkJetPt)
                if (abs(geta)<1.5): foundGenJetB = True
                else: foundGenJetE = True
        if (foundGenJet):
            tkJetPtvsGenPt.Fill(event.genjet_pt[nGenJet],MaxTkJetPt) # 2D histogram
            tkJetPull.Fill(event.genjet_pt[nGenJet]-MaxTkJetPt)
    
        # Efficiencies:
        if (foundGenEmuJet): genJetPassedEmuPt.Fill(event.genjet_pt[nGenJet])
        if (foundGenEmuJetB): genJetPassedEmuPtB.Fill(event.genjet_pt[nGenJet])
        if (foundGenEmuJetE): genJetPassedEmuPtE.Fill(event.genjet_pt[nGenJet])
        if (foundGenJet): genJetPassedPt.Fill(event.genjet_pt[nGenJet])
        if (foundGenJetB): genJetPassedPtB.Fill(event.genjet_pt[nGenJet])
        if (foundGenJetE): genJetPassedPtE.Fill(event.genjet_pt[nGenJet])

    counter+=1 #could just use enumerate...

print("Number Reco Vtx ({}) within 0.5cm of MC Vtx ({}) = {}".format(goodVtx,counter,goodVtx/counter))
# "Entries:\t\t"+('%.0f' % pvResQNN.GetEntries())

outputFile.cd()

#GEN
genPt.Write()
genPhi.Write()
genPID.Write()

#Tracks
trackPt.Write()
trackEta.Write()
trackPhi.Write()
trackChi2.Write()
trackMVA.Write()
trackFake.Write()
trackz0.Write()

#PV
pvReco.Write()
pvMC.Write()
pvRes.Write()
pvResEmu.Write()

#MET
tpEta.Write()
tpPt.Write()
tpMatchedEta.Write()
tpMatchedPt.Write()
denMET.Write()
numMET.Write()
METRes.Write()

#Jets
genJetPt.Write()
genJetPtB.Write()
genJetPtE.Write()
genJetPassedPt.Write()
genJetPassedPtB.Write()
genJetPassedPtE.Write()
genJetPassedEmuPt.Write()
genJetPassedEmuPtB.Write()
genJetPassedEmuPtE.Write()
tkJetPt.Write()
tkJetEmuPt.Write()
tkJetPtvsGenPt.Write()
tkJetEmuPtvsGenPt.Write()
tkJetEmuPull.Write()
tkJetPull.Write()

outputFile.Close()
