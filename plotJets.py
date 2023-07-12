import numpy
import ROOT
from ROOT import *

DY=False
TT=False
TTSL=False
ZP=False
### Switch ###
# DY=True
TT=True
# TTSL=True
# ZP=True

### Macros ###
def plot(canvas,name):
    canvas.Print(name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetLineWidth(2)
    hist.SetMarkerColor(value)
    # hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.8)
    hist.SetMarkerSize(1.0)
    # hist.Draw("")
    # hist.Paint("")
    # hist.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,500.0)
    # hist.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
    # hist.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)

def setCanvas(canvas):
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.08)
    canvas.SetTopMargin(0.08)


# Labels
ptCMS = TPaveText(0.12,0.925,0.205,0.99,"NDC")
ptCMS.AddText("CMS")
ptCMS.SetTextAlign(13)
ptCMS.SetTextFont(62)
ptCMS.SetTextSize(0.04)
ptCMS.SetBorderSize(0)
ptCMS.SetFillColor(0)

ptP2Sim = TPaveText(0.205,0.925,0.44,0.97,"NDC")
ptP2Sim.AddText("Phase-2 Simulation")
ptP2Sim.SetTextAlign(13)
ptP2Sim.SetTextFont(72)
ptP2Sim.SetTextSize(0.025)
ptP2Sim.SetBorderSize(0)
ptP2Sim.SetFillColor(0)

ptEandPU = TPaveText(0.64,0.925,0.92,0.975,"NDC")
ptEandPU.AddText("14 TeV, 200 PU")
ptEandPU.SetTextAlign(33)
ptEandPU.SetTextFont(62)
ptEandPU.SetTextSize(0.03)
ptEandPU.SetBorderSize(0)
ptEandPU.SetFillColor(0)

# ptSample = TPaveText(0.65,0.35,0.83,0.40,"NDC") #RHS
ptSample = TPaveText(0.15,0.35,0.33,0.40,"NDC") #LHS
if DY: ptSample.AddText("DYToLL M-50")
if TT: ptSample.AddText("TT TuneCP5")
if TTSL: ptSample.AddText("TTSL")
if ZP: ptSample.AddText("ZprimeToMuMu M-6000")
ptSample.SetTextAlign(11)
ptSample.SetTextFont(52)
ptSample.SetTextSize(0.03)
ptSample.SetBorderSize(0)
ptSample.SetFillColor(0)

### Binning ###
# PtBins=numpy.array([0.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 200.0, 400.0])
PtBins=numpy.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 175.0, 200.0, 250.0, 300.0, 400.0, 500.0, 600.0, 800.0, 1000.0])
nPtBins=len(PtBins)-1

EtaBins=numpy.array([-2.5,-2.1,-1.6,-1.2,-0.9,-0.3,0.3,0.9,1.2,1.6,2.1,2.5])
nEtaBins=len(EtaBins)-1

pi=3.14
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
nPhiBins=len(PhiBins)-1

### Style ###
gStyle.SetOptStat("")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

### Make plots ###
f=ROOT.TFile("PVPlots_TTFall22PUTP_tkJets.root")

f.cd()
denJetPt = f.Get("genJetPt")
numJetPt = f.Get("genJetPassedPt")
numJetEmuPt = f.Get("genJetPassedEmuPt")
denJetPtB = f.Get("genJetPtB")
numJetPtB = f.Get("genJetPassedPtB")
numJetEmuPtB = f.Get("genJetPassedEmuPtB")
denJetPtE = f.Get("genJetPtE")
numJetPtE = f.Get("genJetPassedPtE")
numJetEmuPtE = f.Get("genJetPassedEmuPtE")

# denJetPt.Rebin(5)
# numJetPt.Rebin(5)
# numJetEmuPt.Rebin(5)
denJetPt.Rebin(nPtBins,"dJetPt",PtBins)
numJetPt.Rebin(nPtBins,"nJetPt",PtBins)
numJetEmuPt.Rebin(nPtBins,"nEmuPt",PtBins)
dJetPt=ROOT.gDirectory.Get("dJetPt")
nJetPt=ROOT.gDirectory.Get("nJetPt")
nEmuPt=ROOT.gDirectory.Get("nEmuPt")

denJetPtB.Rebin(nPtBins,"dJetPtB",PtBins)
numJetPtB.Rebin(nPtBins,"nJetPtB",PtBins)
numJetEmuPtB.Rebin(nPtBins,"nEmuPtB",PtBins)
dJetPtB=ROOT.gDirectory.Get("dJetPtB")
nJetPtB=ROOT.gDirectory.Get("nJetPtB")
nEmuPtB=ROOT.gDirectory.Get("nEmuPtB")

denJetPtE.Rebin(nPtBins,"dJetPtE",PtBins)
numJetPtE.Rebin(nPtBins,"nJetPtE",PtBins)
numJetEmuPtE.Rebin(nPtBins,"nEmuPtE",PtBins)
dJetPtE=ROOT.gDirectory.Get("dJetPtE")
nJetPtE=ROOT.gDirectory.Get("nJetPtE")
nEmuPtE=ROOT.gDirectory.Get("nEmuPtE")



################################################
#### Plot the Jet efficiency of All TkJets: ####
cEffPt = TCanvas("cEffPt", "cEffPt", 700, 700)
setCanvas(cEffPt)
# effPt = ROOT.TEfficiency(numJetPt,denJetPt)
effPt = ROOT.TEfficiency(nJetPt,dJetPt)
effPt.SetTitle(";genJet p_{T} (GeV);Efficiency")
setStyle(effPt,1)
effPt.SetMarkerStyle(20)
effPt.Draw("")
effPt.Paint("")
effPt.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,500.0)
effPt.GetPaintedGraph().GetYaxis().SetRangeUser(0.0,1.0)
effPt.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPt.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)

# # effEmuPt = ROOT.TEfficiency(numJetEmuPt,denJetPt)
effEmuPt = ROOT.TEfficiency(nEmuPt,dJetPt)
setStyle(effEmuPt,2)
effEmuPt.SetMarkerStyle(21)
effEmuPt.Draw("same")

# Add labels:
ptCMS.Draw("same")
ptP2Sim.Draw("same")
ptEandPU.Draw("same")
ptSample.Draw("same")

ptRegion = TPaveText(0.45,0.25,0.83,0.30,"NDC")
ptRegion.AddText("All. p_{T}>50. dR<0.4")
ptRegion.SetTextAlign(11)
ptRegion.SetTextFont(52)
ptRegion.SetTextSize(0.03)
ptRegion.SetBorderSize(0)
ptRegion.SetFillColor(0)
ptRegion.Draw("same")

# Legend:
leg = ROOT.TLegend(0.45,0.15,0.83,0.25)
leg.AddEntry(effPt,"TkJet Simulation","p")
leg.AddEntry(effEmuPt,"TkJet Emulation","p")
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

plot(cEffPt,"TkJetEffVsGenJetPt")

###################################################
#### Plot the Jet efficiency of Barrel TkJets: ####
cEffPtB = TCanvas("cEffPtB", "cEffPtB", 700, 700)
setCanvas(cEffPtB)
effPtB = ROOT.TEfficiency(nJetPtB,dJetPtB)
effPtB.SetTitle(";genJet p_{T} (GeV);Efficiency")
setStyle(effPtB,1)
effPtB.SetMarkerStyle(20)
effPtB.Draw("")
effPtB.Paint("")
effPtB.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,500.0)
effPtB.GetPaintedGraph().GetYaxis().SetRangeUser(0.0,1.0)
effPtB.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPtB.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)

effEmuPtB = ROOT.TEfficiency(nEmuPtB,dJetPtB)
setStyle(effEmuPtB,2)
effEmuPtB.SetMarkerStyle(21)
effEmuPtB.Draw("same")

# Add labels:
ptCMS.Draw("same")
ptP2Sim.Draw("same")
ptEandPU.Draw("same")
ptSample.Draw("same")

ptRegion = TPaveText(0.45,0.25,0.83,0.30,"NDC")
# ptRegion.AddText("Barrel. No p_{T} cuts. dR<0.4")
ptRegion.AddText("Barrel. p_{T}>50. dR<0.4")
ptRegion.SetTextAlign(11)
ptRegion.SetTextFont(52)
ptRegion.SetTextSize(0.03)
ptRegion.SetBorderSize(0)
ptRegion.SetFillColor(0)
ptRegion.Draw("same")

# Legend:
leg = ROOT.TLegend(0.45,0.15,0.83,0.25)
leg.AddEntry(effPtB,"TkJet Simulation","p")
leg.AddEntry(effEmuPtB,"TkJet Emulation","p")
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

plot(cEffPtB,"TkJetEffVsGenJetPtB")


###################################################
#### Plot the Jet efficiency of Endcap TkJets: ####
cEffPtE = TCanvas("cEffPtE", "cEffPtE", 700, 700)
setCanvas(cEffPtE)
effPtE = ROOT.TEfficiency(nJetPtE,dJetPtE)
effPtE.SetTitle(";genJet p_{T} (GeV);Efficiency")
setStyle(effPtE,1)
effPtE.SetMarkerStyle(20)
effPtE.Draw("")
effPtE.Paint("")
effPtE.GetPaintedGraph().GetXaxis().SetRangeUser(0.0,500.0)
effPtE.GetPaintedGraph().GetYaxis().SetRangeUser(0.0,1.0)
effPtE.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPtE.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)

effEmuPtE = ROOT.TEfficiency(nEmuPtE,dJetPtE)
setStyle(effEmuPtE,2)
effEmuPtE.SetMarkerStyle(21)
effEmuPtE.Draw("same")

# Add labels:
ptCMS.Draw("same")
ptP2Sim.Draw("same")
ptEandPU.Draw("same")
ptSample.Draw("same")

ptRegion = TPaveText(0.45,0.25,0.83,0.30,"NDC")
# ptRegion.AddText("Endcap. No p_{T} cuts. dR<0.4")
ptRegion.AddText("Endcap. p_{T}>50. dR<0.4")
ptRegion.SetTextAlign(11)
ptRegion.SetTextFont(52)
ptRegion.SetTextSize(0.03)
ptRegion.SetBorderSize(0)
ptRegion.SetFillColor(0)
ptRegion.Draw("same")

# Legend:
leg = ROOT.TLegend(0.45,0.15,0.83,0.25)
leg.AddEntry(effPtE,"TkJet Simulation","p")
leg.AddEntry(effEmuPtE,"TkJet Emulation","p")
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

plot(cEffPtE,"TkJetEffVsGenJetPtE")



gStyle.SetPalette(1)

#########################################
#### Plot the TkJet pT vs GenJet pT: ####
cJetPtvsGenPt = TCanvas("cJetPtvsGenPt", "cJetPtvsGenPt", 700, 700)
setCanvas(cJetPtvsGenPt)
cJetPtvsGenPt.SetRightMargin(0.15)

tkJetPtvsGenPt=f.Get("tkJetPtvsGenPt")
tkJetPtvsGenPt.SetTitle(";GenJet p_{T} (GeV);TkJet (Simulated) p_{T} (GeV)")
tkJetPtvsGenPt.SetContour(99)
tkJetPtvsGenPt.GetXaxis().SetTitleOffset(1.4)
tkJetPtvsGenPt.GetYaxis().SetTitleOffset(1.65)
tkJetPtvsGenPt.Rebin2D(5,5,"tkJetPtvsGenPt5")
tkJetPtvsGenPt5=ROOT.gDirectory.Get("tkJetPtvsGenPt5")

tkJetPtvsGenPt5.GetXaxis().SetRangeUser(0.0,700.0)
tkJetPtvsGenPt5.GetYaxis().SetRangeUser(0.0,700.0)
tkJetPtvsGenPt5.GetZaxis().SetRangeUser(0.0,3000.0)
tkJetPtvsGenPt5.Draw("COLZ")
plot(cJetPtvsGenPt,"TkJetPtVsGenJetPt")

# Zoom in on interesting region
tkJetPtvsGenPt.GetXaxis().SetRangeUser(50.0,150.0)
tkJetPtvsGenPt.GetYaxis().SetRangeUser(50.0,150.0)
tkJetPtvsGenPt.GetZaxis().SetRangeUser(0.0,200.0)
tkJetPtvsGenPt.Draw("COLZ")
plot(cJetPtvsGenPt,"TkJetPtVsGenJetPtZoom")



#########################################
#### Plot the TkJet pT vs GenJet pT: ####
cJetEmuPtvsGenPt = TCanvas("cJetEmuPtvsGenPt", "cJetEmuPtvsGenPt", 700, 700)
setCanvas(cJetEmuPtvsGenPt)
cJetEmuPtvsGenPt.SetRightMargin(0.15)

tkJetEmuPtvsGenPt=f.Get("tkJetEmuPtvsGenPt")
tkJetEmuPtvsGenPt.SetTitle(";GenJet p_{T} (GeV);TkJet (Emulated) p_{T} (GeV)")
tkJetEmuPtvsGenPt.SetContour(99)
tkJetEmuPtvsGenPt.GetXaxis().SetTitleOffset(1.4)
tkJetEmuPtvsGenPt.GetYaxis().SetTitleOffset(1.65)
tkJetEmuPtvsGenPt.Rebin2D(5,5,"tkJetEmuPtvsGenPt5")
tkJetEmuPtvsGenPt5=ROOT.gDirectory.Get("tkJetEmuPtvsGenPt5")

tkJetEmuPtvsGenPt5.GetXaxis().SetRangeUser(0.0,700.0)
tkJetEmuPtvsGenPt5.GetYaxis().SetRangeUser(0.0,700.0)
tkJetEmuPtvsGenPt5.GetZaxis().SetRangeUser(0.0,3000.0)
tkJetEmuPtvsGenPt5.Draw("COLZ")
plot(cJetEmuPtvsGenPt,"TkJetEmuPtVsGenJetPt")

# Zoom in on interesting region
# gStyle.SetPalette(kDarkBodyRadiator)
tkJetEmuPtvsGenPt.GetXaxis().SetRangeUser(50.0,150.0)
tkJetEmuPtvsGenPt.GetYaxis().SetRangeUser(50.0,150.0)
tkJetEmuPtvsGenPt.GetZaxis().SetRangeUser(0.0,200.0)
tkJetEmuPtvsGenPt.Draw("COLZ")
plot(cJetEmuPtvsGenPt,"TkJetEmuPtVsGenJetPtZoom")



##############################
#### Plot the TkJet Pull: ####
cJetPull = TCanvas("cJetPull", "cJetPull", 700, 700)
setCanvas(cJetPull)
jetPull = f.Get("tkJetPull")
jetPull.Rebin(2)
jetPull.SetTitle(";genJet p_{T}-TrkJet p_{T} [GeV];")
setStyle(jetPull,1)
jetPull.SetMarkerStyle(20)
jetPull.Draw("")
jetPull.GetXaxis().SetRangeUser(-200.0,200.0)
jetPull.GetYaxis().SetRangeUser(0.0,18000.0)
jetPull.GetXaxis().SetTitleOffset(1.4)
jetPull.GetYaxis().SetTitleOffset(1.65)

jetEmuPull = f.Get("tkJetEmuPull")
jetEmuPull.Rebin(2)
setStyle(jetEmuPull,2)
jetEmuPull.SetMarkerStyle(21)
jetEmuPull.Draw("same")

# Add labels:
ptCMS.Draw("same")
ptP2Sim.Draw("same")
ptEandPU.Draw("same")
ptSample.Draw("same")

ptRegion = TPaveText(0.15,0.30,0.33,0.35,"NDC")
ptRegion.AddText("All. p_{T}>30. dR<0.4")
ptRegion.SetTextAlign(11)
ptRegion.SetTextFont(52)
ptRegion.SetTextSize(0.03)
ptRegion.SetBorderSize(0)
ptRegion.SetFillColor(0)
ptRegion.Draw("same")

# Legend:
leg = ROOT.TLegend(0.15,0.20,0.33,0.30)
leg.AddEntry(jetPull,"TkJet Simulation","l")
leg.AddEntry(jetEmuPull,"TkJet Emulation","l")
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

plot(cJetPull,"TkJetPulls")
