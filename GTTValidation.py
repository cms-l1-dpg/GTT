import ROOT
import array
from datetime import datetime
import os

now=datetime.now()
workArea = 'GTTValidation_{:s}'.format(now.strftime("%Y-%m-%d"))
if not os.path.exists(workArea):
    os.makedirs(workArea)

### Input Files ###
# Here we are reading in files created from anaL1TrackNtuple.py
# anaL1TrackNtuple.py ran over ntuples created from L1Trigger/L1TTrackMatch/test/L1TrackObjectNtupleMaker_cfg.py
fReference=ROOT.TFile("Reference.root")
fTarget=ROOT.TFile("Target.root")
RefName="Reference"
TarName="Target"

### Macros ###
def plot(canvas,name):

    canvas.Print(workArea+"/"+name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetLineWidth(2)
    hist.SetMarkerColor(value)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.8)
    # hist.SetMarkerSize(1.0)
    # hist.Draw("")
    # hist.Paint("")
    hist.GetXaxis().SetTitleOffset(1.4)
    hist.GetYaxis().SetTitleOffset(1.65)

def setCanvas(canvas):
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.08)
    canvas.SetTopMargin(0.08)

def addLeg(Ref, Tar, RefLabel, TarLabel, leg):
    leg.AddEntry(Ref,RefLabel,"l")
    leg.AddEntry(Tar,TarLabel,"l")
    leg.SetTextFont(42)
    leg.SetTextSize(0.03)
    leg.SetMargin(0.15)
    leg.SetFillColor(0)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(0)
    leg.Draw("hist")

def addStats(Ref,Tar,ptRef,ptTar):
    dEntRef    = "Entries:\t\t"+('%.0f' % Ref.GetEntries())
    dMeanRef   = "Mean:\t\t\t\t"+('%.3f' % Ref.GetMean())
    dStdDevRef = "StdDev:\t"+('%.3f' % Ref.GetStdDev())
    print ("Ref:")
    print ("\t",dEntRef)
    print ("\t",dMeanRef)
    print ("\t",dStdDevRef)
    dEntTar    = "Entries:\t\t"+('%.0f' % Tar.GetEntries())
    dMeanTar   = "Mean:\t\t\t\t"+('%.3f' % Tar.GetMean())
    dStdDevTar = "StdDev:\t"+('%.3f' % Tar.GetStdDev())
    print ("Tar:")
    print ("\t",dEntTar)
    print ("\t",dMeanTar)
    print ("\t",dStdDevTar)

    # ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
    ptRef.AddText(dEntRef)
    ptRef.AddText(dMeanRef)
    ptRef.AddText(dStdDevRef)
    ptRef.SetBorderSize(0)
    ptRef.SetFillColor(0)
    ptRef.SetLineColor(ROOT.kBlack)
    ptRef.SetTextAlign(12)
    ptRef.SetTextColor(ROOT.kBlack)
    ptRef.SetTextFont(42)
    ptRef.SetTextSize(0.03)
    ptRef.Draw("same")

    # ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
    ptTar.AddText(dEntTar)
    ptTar.AddText(dMeanTar)
    ptTar.AddText(dStdDevTar)
    ptTar.SetBorderSize(0)
    ptTar.SetFillColor(0)
    ptTar.SetLineColor(ROOT.kRed)
    ptTar.SetTextAlign(12)
    ptTar.SetTextColor(ROOT.kRed)
    ptTar.SetTextFont(42)
    ptTar.SetTextSize(0.03)
    ptTar.Draw("same")

# def writeCMS(canvas):
#     canvas.cd()

### Binning ###
PtBins=array.array('d',[0.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 200.0, 400.0])
nPtBins=len(PtBins)-1

EtaBins=array.array('d',[-2.5,-2.1,-1.6,-1.2,-0.9,-0.3,0,0.3,0.9,1.2,1.6,2.1,2.5])
nEtaBins=len(EtaBins)-1

pi=3.14
PhiBins=array.array('d',[-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
nPhiBins=len(PhiBins)-1

### Style ###
ROOT.gStyle.SetOptStat("")
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)


######################
### 1. Gen Objects ###
######################

### 1.1 Gen pT ###
cGenPt = ROOT.TCanvas("cGenPt", "cGenPt", 700, 700)
setCanvas(cGenPt)
GenPtRef=fReference.Get("genPt")
GenPtRef.SetTitle("Gen p_{T};Gen p_{T} [GeV];Entries")
setStyle(GenPtRef,1)
GenPtRef.Draw()
GenPtTar=fTarget.Get("genPt")
setStyle(GenPtTar,2)
GenPtTar.Draw("same")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(GenPtRef, GenPtTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(GenPtRef,GenPtTar,ptRef,ptTar)
GenPtRef.GetXaxis().SetRangeUser(0.0,70.0)
cGenPt.SetLogy()
plot(cGenPt,"GTTValidation_11_GenPt")

### 1.2 Gen phi ###
cGPhi = ROOT.TCanvas("cGPhi", "cGPhi", 700, 700)
setCanvas(cGPhi)
genPhiRef=fReference.Get("genPhi")
genPhiRef.SetTitle("Gen #phi;Gen #phi;Entries")
setStyle(genPhiRef,1)
genPhiRef.Rebin(2)
genPhiRef.GetXaxis().SetRangeUser(-3.4,3.4)
genPhiRef.Draw("ep")
genPhiTar=fTarget.Get("genPhi")
setStyle(genPhiTar,2)
genPhiTar.Rebin(2)
genPhiTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(genPhiRef, genPhiTar, RefName, TarName, leg)
plot(cGPhi,"GTTValidation_12_GenPhi")

### 1.3 Gen PID ###
cGPID = ROOT.TCanvas("cGPID", "cGPID", 700, 700)
setCanvas(cGPID)
genPIDRef=fReference.Get("genPID")
genPIDRef.SetTitle("Gen PDG ID;Gen PDG ID;Entries")
setStyle(genPIDRef,1)
genPIDRef.GetXaxis().SetRangeUser(-330.0,330.0)
genPIDRef.Draw("ep")
genPIDTar=fTarget.Get("genPID")
setStyle(genPIDTar,2)
genPIDTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(genPIDRef, genPIDTar, RefName, TarName, leg)
plot(cGPID,"GTTValidation_13_GenPID")

### 1.4 Gen PV ###
cGPV = ROOT.TCanvas("cGPV", "cGPV", 700, 700)
setCanvas(cGPV)
genPVRef=fReference.Get("pvReco")
genPVRef.SetTitle("Gen PV;PV z0 [cm];Entries")
setStyle(genPVRef,1)
genPVRef.Rebin(5)
genPVRef.GetXaxis().SetRangeUser(-20.0,20.0)
genPVRef.Draw("ep")
genPVTar=fTarget.Get("pvReco")
setStyle(genPVTar,2)
genPVTar.Rebin(5)
genPVTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(genPIDRef, genPIDTar, RefName, TarName, leg)
plot(cGPV,"GTTValidation_14_GenPV")

### 1.5 GenJet pT ###
cGenJetPt = ROOT.TCanvas("cGenJetPt", "cGenJetPt", 700, 700)
setCanvas(cGenJetPt)
genJetPtRef=fReference.Get("genJetPt")
genJetPtRef.SetTitle("Gen Jet p_{T};Gen Jet p_{T} [GeV];Number of Gen Jets/GeV")
setStyle(genJetPtRef,1)
genJetPtRef.Draw()
genJetPtTar=fTarget.Get("genJetPt")
setStyle(genJetPtTar,2)
genJetPtTar.Draw("same")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(genJetPtRef, genJetPtTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(genJetPtRef,genJetPtTar,ptRef,ptTar)
genJetPtRef.GetXaxis().SetRangeUser(0.0,70.0)
cGenJetPt.SetLogy()
plot(cGenJetPt,"GTTValidation_15_GenJetPt")

### 1.6 GenMET ###
cGenMET = ROOT.TCanvas("cGenMET", "cGenMET", 700, 700)
setCanvas(cGenMET)
genMETRef=fReference.Get("denMET")
genMETRef.SetTitle("Gen MET;Gen MET [GeV];Entries")
setStyle(genMETRef,1)
genMETRef.Rebin(10)
genMETRef.Draw("ep")
genMETTar=fTarget.Get("denMET")
setStyle(genMETTar,2)
genMETTar.Rebin(10)
genMETTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(genMETRef, genMETTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(genMETRef,genMETTar,ptRef,ptTar)
genMETRef.GetXaxis().SetRangeUser(0.0,300.0)
cGenMET.SetLogy()
plot(cGenMET,"GTTValidation_16_GenMET")


#################
### 2. Tracks ###
#################

### 2.1 Track pT ###
cPt = ROOT.TCanvas("cPt", "cPt", 700, 700)
setCanvas(cPt)
trackPtRef=fReference.Get("trackPt")
trackPtRef.SetTitle("Track p_{T};Track p_{T} [GeV];Number of tracks/GeV")
setStyle(trackPtRef,1)
trackPtRef.Draw()
trackPtTar=fTarget.Get("trackPt")
setStyle(trackPtTar,2)
trackPtTar.Draw("same")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(trackPtRef, trackPtTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(trackPtRef,trackPtTar,ptRef,ptTar)
trackPtRef.GetXaxis().SetRangeUser(0.0,70.0)
cPt.SetLogy()
plot(cPt,"GTTValidation_21_TrackPt")

### 2.2 Track eta - in eta bins ###
cEtaInBins = ROOT.TCanvas("cEtaInBins", "cEtaInBins", 700, 700)
setCanvas(cEtaInBins)
trackEtaInBinsRef=fReference.Get("trackEta")
trackEtaInBinsRef.SetTitle("Track #eta;Track #eta;Number of tracks")
trackEtaInBinsRefRebinned=trackEtaInBinsRef.Rebin(nEtaBins,'trackEtaInBinsRefRebinned',EtaBins)
trackEtaInBinsRefRebinned.GetXaxis().SetRangeUser(-2.6,2.6)
setStyle(trackEtaInBinsRefRebinned,1)
trackEtaInBinsRefRebinned.Draw("ep")

trackEtaInBinsTar=fTarget.Get("trackEta")
trackEtaInBinsTarRebinned=trackEtaInBinsTar.Rebin(nEtaBins,'trackEtaInBinsTarRebinned',EtaBins)
setStyle(trackEtaInBinsTarRebinned,2)
trackEtaInBinsTarRebinned.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackEtaInBinsRefRebinned, trackEtaInBinsTarRebinned, RefName, TarName, leg)
plot(cEtaInBins,"GTTValidation_22_TrackEtaInBins")


### 2.2 Track eta ###
cEta = ROOT.TCanvas("cEta", "cEta", 700, 700)
setCanvas(cEta)
trackEtaRef=fReference.Get("trackEta")
trackEtaRef.SetTitle("Track #eta;Track #eta;Number of tracks")
setStyle(trackEtaRef,1)
trackEtaRef.Rebin(2)
trackEtaRef.GetXaxis().SetRangeUser(-2.6,2.6)
trackEtaRef.Draw("ep")

trackEtaTar=fTarget.Get("trackEta")
setStyle(trackEtaTar,2)
trackEtaTar.Rebin(2)
trackEtaTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackEtaRef, trackEtaTar, RefName, TarName, leg)
plot(cEta,"GTTValidation_22_TrackEta")

### 2.3 Track phi ###
cPhi = ROOT.TCanvas("cPhi", "cPhi", 700, 700)
setCanvas(cPhi)
trackPhiRef=fReference.Get("trackPhi")
trackPhiRef.SetTitle("Track #phi;Track #phi;Number of tracks")
setStyle(trackPhiRef,1)
trackPhiRef.Rebin(2)
trackPhiRef.GetXaxis().SetRangeUser(-3.4,3.4)
trackPhiRef.Draw("ep")
trackPhiTar=fTarget.Get("trackPhi")
setStyle(trackPhiTar,2)
trackPhiTar.Rebin(2)
trackPhiTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackPhiRef, trackPhiTar, RefName, TarName, leg)
plot(cPhi,"GTTValidation_23_TrackPhi")

### 2.4 Track MVA ###
cMVA = ROOT.TCanvas("cMVA", "cMVA", 700, 700)
setCanvas(cMVA)
trackMVARef=fReference.Get("trackMVA")
trackMVARef.SetTitle("Track MVA;Track MVA;Number of tracks")
setStyle(trackMVARef,1)
trackMVARef.Draw("ep")
trackMVATar=fTarget.Get("trackMVA")
setStyle(trackMVATar,2)
trackMVATar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackMVARef, trackMVATar, RefName, TarName, leg)
cMVA.SetLogy()
plot(cMVA,"GTTValidation_24_TrackMVA")

### 2.5 Track Chi2 ###
cTrkChi2 = ROOT.TCanvas("cTrkChi2", "cTrkChi2", 700, 700)
setCanvas(cTrkChi2)
trackChi2Ref=fReference.Get("trackChi2")
trackChi2Ref.SetTitle("Track Chi2;Chi2;Number of tracks")
setStyle(trackChi2Ref,1)
trackChi2Ref.Draw("")
trackChi2Tar=fTarget.Get("trackChi2")
setStyle(trackChi2Tar,2)
trackChi2Tar.Draw("same")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(trackChi2Ref, trackChi2Tar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(trackChi2Ref,trackChi2Tar,ptRef,ptTar)
cTrkChi2.SetLogy()
plot(cTrkChi2,"GTTValidation_25_TrackChi2")

### 2.6 Track Fakes ###
cTrkFake = ROOT.TCanvas("cTrkFake", "cTrkFake", 700, 700)
setCanvas(cTrkFake)
trackFakeRef=fReference.Get("trackFake")
trackFakeRef.SetTitle("Track Fakes;Fake Quality;Number of tracks")
setStyle(trackFakeRef,1)
trackFakeRef.Draw("")
trackFakeTar=fTarget.Get("trackFake")
setStyle(trackFakeTar,2)
trackFakeTar.Draw("same")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackFakeRef, trackFakeTar, RefName, TarName, leg)
plot(cTrkFake,"GTTValidation_26_TrackFakes")

### 2.7 Track z0 ###
cTrkz0 = ROOT.TCanvas("cTrkz0", "cTrkz0", 700, 700)
setCanvas(cTrkz0)
trackz0Ref=fReference.Get("trackz0")
trackz0Ref.SetTitle("Track z0;z0 [cm];Number of tracks")
setStyle(trackz0Ref,1)
trackz0Ref.Draw("")
trackz0Tar=fTarget.Get("trackz0")
setStyle(trackz0Tar,2)
trackz0Tar.Draw("same")

leg = ROOT.TLegend(0.68,0.24,0.88,0.35)
addLeg(trackz0Ref, trackz0Tar, RefName, TarName, leg)
plot(cTrkz0,"GTTValidation_26_Trackz0")



######################
### 3. GTT Objects ###
######################

### 3.1 & 3.2 PV Res ###
cPVRes = ROOT.TCanvas("cPVRes", "cPVRes", 700, 700)
setCanvas(cPVRes)
pvResRef=fReference.Get("pvResEmu")
pvResRef.SetTitle("Emulated PV Resolution;z_{0}^{PV} Residual [cm];Events")
setStyle(pvResRef,1)
pvResRef.Draw("ep")
pvResTar=fTarget.Get("pvResEmu")
setStyle(pvResTar,2)
pvResTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(pvResRef, pvResTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(pvResRef,pvResTar,ptRef,ptTar)

pvResRef.GetXaxis().SetRangeUser(-20.0,20.0)
cPVRes.SetLogy()
plot(cPVRes,"GTTValidation_31_GTTPVResEmu")

pvResRef.GetXaxis().SetRangeUser(-1.0,1.0)
pvResRef.GetYaxis().SetRangeUser(2,100.)
plot(cPVRes,"GTTValidation_32_GTTPVResEmuZoom")

### 3.3 TkJet Emu Pt ###
cTkJetPt = ROOT.TCanvas("cTkJetPt", "cTkJetPt", 700, 700)
setCanvas(cTkJetPt)
tkJetPtRef=fReference.Get("tkJetEmuPt")
tkJetPtRef.SetTitle("Emulated TkJet p_{T};Emulated TkJet p_{T} [GeV];Entries")
setStyle(tkJetPtRef,1)
tkJetPtRef.Draw()
tkJetPtTar=fTarget.Get("tkJetEmuPt")
setStyle(tkJetPtTar,2)
tkJetPtTar.Draw("same")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(tkJetPtRef, tkJetPtTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(tkJetPtRef,tkJetPtTar,ptRef,ptTar)
tkJetPtRef.GetXaxis().SetRangeUser(0.0,70.0)
cTkJetPt.SetLogy()
plot(cTkJetPt,"GTTValidation_33_GTTTkJetEmuPt")

### 3.4 TkJet Emu Pull ###
cTkJetPull = ROOT.TCanvas("cTkJetPull", "cTkJetPull", 700, 700)
setCanvas(cTkJetPull)
tkJetPullRef=fReference.Get("tkJetEmuPull")
tkJetPullRef.SetTitle("Emulated TkJet Pull;Generated Jet p_{T} - Emulated TkJet p_{T} [GeV];Entries")
setStyle(tkJetPullRef,1)
tkJetPullRef.Rebin(20)
tkJetPullRef.Draw("ep")
tkJetPullTar=fTarget.Get("tkJetEmuPull")
setStyle(tkJetPullTar,2)
tkJetPullTar.Rebin(20)
tkJetPullTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(tkJetPullRef, tkJetPullTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(tkJetPullRef,tkJetPullTar,ptRef,ptTar)
# tkJetPullRef.GetXaxis().SetRangeUser(0.0,70.0)
# cTkJetPull.SetLogy()
plot(cTkJetPull,"GTTValidation_34_GTTTkJetEmuPull")

### 3.5 MET Res ###
cMETRes = ROOT.TCanvas("cMETRes", "cMETRes", 700, 700)
setCanvas(cMETRes)
METResRef=fReference.Get("METRes")
METResRef.SetTitle("MET Resolution;(Emulated MET - Generated MET)/Generated MET;Entries")
setStyle(METResRef,1)
METResRef.Rebin(10)
METResRef.Draw("ep")
METResTar=fTarget.Get("METRes")
setStyle(METResTar,2)
METResTar.Rebin(10)
METResTar.Draw("epsame")

leg = ROOT.TLegend(0.68,0.44,0.88,0.55)
addLeg(METResRef, METResTar, RefName, TarName, leg)
ptRef = ROOT.TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptTar = ROOT.TPaveText(0.68,0.66,0.88,0.77,"NDC")
addStats(METResRef,METResTar,ptRef,ptTar)
METResRef.GetXaxis().SetRangeUser(0.0,15.0)
# cMETRes.SetLogy()
plot(cMETRes,"GTTValidation_35_GTTMETRes")

### 3.X Triplets? ###

