import numpy
import ROOT
from ROOT import *

DY=False
TT=False
TTSL=False
ZP=False
DarkSUSY=False
### Switch ###
# DY=True
TT=True
# TTSL=True
# ZP=True
# DarkSUSY=True

### Macros ###
def plot(canvas,name):
    canvas.Print(name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetLineWidth(2)
    hist.SetMarkerColor(value)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.8)
    # hist.SetMarkerSize(1.0)
    hist.Draw("")
    hist.Paint("")
    hist.GetXaxis().SetTitleOffset(1.4)
    hist.GetYaxis().SetTitleOffset(1.65)

def setCanvas(canvas):
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.08)
    canvas.SetTopMargin(0.08)

### Binning ###
PtBins=numpy.array([0.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 200.0, 400.0])
nPtBins=len(PtBins)-1

EtaBins=numpy.array([-2.5,-2.1,-1.6,-1.2,-0.9,-0.3,0.3,0.9,1.2,1.6,2.1,2.5])
nEtaBins=len(EtaBins)-1

pi=3.14
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
nPhiBins=len(PhiBins)-1

### Style ###
gStyle.SetOptStat("")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

### Make plots ###
if DY:
    f=ROOT.TFile("PVPlots_DYFall22PUTP_FHE_MCPVM3RunPV.root")
if TT:
    f=ROOT.TFile("PVPlots_TTFall22PUTP_FHE_MCPVM3RunPV.root")
if TTSL:
    f=ROOT.TFile("PVPlots_TTSLFall22PUTP_FHE_MCPVM3RunPV.root")
if ZP:
    f=ROOT.TFile("PVPlots_ZMM.root")
if DarkSUSY:
    f=ROOT.TFile("PVPlots_DarkSUSYFall22PUTP_tkJets.root")


##############################################
#### Plot the Z0 Resolution of FH and NN: ####
cPVRes = TCanvas("cPVRes", "cPVRes", 700, 700)
setCanvas(cPVRes)
f.cd()
pvResFH=f.Get("pvRes")
pvResFH.SetTitle(";z_{0}^{PV} Residual [cm];Events")
setStyle(pvResFH,kBlack)
# pvResFH.Rebin(5)

# pvResNNEmu=f.Get("pvResEmu")
# setStyle(pvResNNEmu,kRed)
# pvResNNEmu.Rebin(5)

pvResFHEmu=f.Get("pvResEmu")
setStyle(pvResFHEmu,kBlue)

pvResFH.Draw("ep")
# pvResNNEmu.SetMarkerStyle(kOpenCircle)
# pvResNNEmu.Draw("epsame")
pvResFHEmu.SetMarkerStyle(kOpenSquare)
pvResFHEmu.Draw("epsame")

leg = ROOT.TLegend(0.16,0.73,0.36,0.83)
leg.AddEntry(pvResFH,"FH Simulation","p")
# leg.AddEntry(pvResNNEmu,"NN Emulation","p")
leg.AddEntry(pvResFHEmu,"FH Emulation","p")
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

dEntpvResFH    = "Entries:\t\t"+('%.0f' % pvResFH.GetEntries())
dMeanpvResFH   = "Mean:\t\t\t\t"+('%.3f' % pvResFH.GetMean())
dStdDevpvResFH = "StdDev:\t"+('%.3f' % pvResFH.GetStdDev())
print ("FH:")
print ("\t",dEntpvResFH)
print ("\t",dMeanpvResFH)
print ("\t",dStdDevpvResFH)

# dEntpvResNNEmu    = "Entries:\t\t"+('%.0f' % pvResNNEmu.GetEntries())
# dMeanpvResNNEmu   = "Mean:\t\t\t\t"+('%.3f' % pvResNNEmu.GetMean())
# dStdDevpvResNNEmu = "StdDev:\t"+('%.3f' % pvResNNEmu.GetStdDev())
# print ("NNEmu:")
# print ("\t",dEntpvResNNEmu)
# print ("\t",dMeanpvResNNEmu)
# print ("\t",dStdDevpvResNNEmu)

dEntpvResFHEmu    = "Entries:\t\t"+('%.0f' % pvResFHEmu.GetEntries())
dMeanpvResFHEmu   = "Mean:\t\t\t\t"+('%.3f' % pvResFHEmu.GetMean())
dStdDevpvResFHEmu = "StdDev:\t"+('%.3f' % pvResFHEmu.GetStdDev())
print ("FHEmu:")
print ("\t",dEntpvResFHEmu)
print ("\t",dMeanpvResFHEmu)
print ("\t",dStdDevpvResFHEmu)

ptpvResFH = TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptpvResFH.AddText(dEntpvResFH)
ptpvResFH.AddText(dMeanpvResFH)
ptpvResFH.AddText(dStdDevpvResFH)
ptpvResFH.SetBorderSize(0)
ptpvResFH.SetFillColor(0)
ptpvResFH.SetLineColor(kBlack)
ptpvResFH.SetTextAlign(12)
ptpvResFH.SetTextColor(kBlack)
ptpvResFH.SetTextFont(42)
ptpvResFH.SetTextSize(0.03)
ptpvResFH.Draw("same")

# ptpvResNNEmu = TPaveText(0.68,0.66,0.88,0.77,"NDC")
# ptpvResNNEmu.AddText(dEntpvResNNEmu)
# ptpvResNNEmu.AddText(dMeanpvResNNEmu)
# ptpvResNNEmu.AddText(dStdDevpvResNNEmu)
# ptpvResNNEmu.SetBorderSize(0)
# ptpvResNNEmu.SetFillColor(0)
# ptpvResNNEmu.SetLineColor(kRed)
# ptpvResNNEmu.SetTextAlign(12)
# ptpvResNNEmu.SetTextColor(kRed)
# ptpvResNNEmu.SetTextFont(42)
# ptpvResNNEmu.SetTextSize(0.03)
# ptpvResNNEmu.Draw("same")

ptpvResFHEmu = TPaveText(0.68,0.66,0.88,0.77,"NDC")
# ptpvResFHEmu = TPaveText(0.68,0.55,0.88,0.66,"NDC")
ptpvResFHEmu.AddText(dEntpvResFHEmu)
ptpvResFHEmu.AddText(dMeanpvResFHEmu)
ptpvResFHEmu.AddText(dStdDevpvResFHEmu)
ptpvResFHEmu.SetBorderSize(0)
ptpvResFHEmu.SetFillColor(0)
ptpvResFHEmu.SetLineColor(kBlue)
ptpvResFHEmu.SetTextAlign(12)
ptpvResFHEmu.SetTextColor(kBlue)
ptpvResFHEmu.SetTextFont(42)
ptpvResFHEmu.SetTextSize(0.03)
ptpvResFHEmu.Draw("same")

# writeCMS(cPVRes)
ptCMS = TPaveText(0.12,0.925,0.205,0.99,"NDC")
ptCMS.AddText("CMS")
ptCMS.SetTextAlign(13)
ptCMS.SetTextFont(62)
ptCMS.SetTextSize(0.04)
ptCMS.SetBorderSize(0)
ptCMS.SetFillColor(0)
ptCMS.Draw("same")

ptP2Sim = TPaveText(0.205,0.925,0.44,0.97,"NDC")
ptP2Sim.AddText("Phase-2 Simulation")
ptP2Sim.SetTextAlign(13)
ptP2Sim.SetTextFont(72)
ptP2Sim.SetTextSize(0.025)
ptP2Sim.SetBorderSize(0)
ptP2Sim.SetFillColor(0)
ptP2Sim.Draw("same")

ptEandPU = TPaveText(0.64,0.925,0.92,0.975,"NDC")
ptEandPU.AddText("14 TeV, 200 PU")
ptEandPU.SetTextAlign(33)
ptEandPU.SetTextFont(62)
ptEandPU.SetTextSize(0.03)
ptEandPU.SetBorderSize(0)
ptEandPU.SetFillColor(0)
ptEandPU.Draw("same")

ptSample = TPaveText(0.16,0.83,0.36,0.88,"NDC")
if DY: ptSample.AddText("DYToLL M-50")
if TT: ptSample.AddText("TT TuneCP5")
if TTSL: ptSample.AddText("TTSL")
if ZP: ptSample.AddText("ZprimeToMuMu M-6000")
ptSample.SetTextAlign(11)
# ptSample.SetTextAlign(31)
ptSample.SetTextFont(52)
ptSample.SetTextSize(0.03)
ptSample.SetBorderSize(0)
ptSample.SetFillColor(0)
ptSample.Draw("same")

# pvResFH.GetXaxis().SetRangeUser(-1.,1.)
if DY: plot(cPVRes,"DY-PVRes")
if TT: plot(cPVRes,"TTbar-PVRes")
if TTSL: plot(cPVRes,"TTSL-PVRes")
if ZP: plot(cPVRes,"ZPMM-PVRes")
if DarkSUSY: plot(cPVRes,"DarkSUSY-PVRes")
cPVRes.SetLogy()

pvResFH.GetXaxis().SetRangeUser(-1.,1.)
if DY:
    pvResFH.GetYaxis().SetRangeUser(200.,50000.)
    plot(cPVRes,"DY-PVRes-LogY")
if TT:
    pvResFH.GetYaxis().SetRangeUser(300.,20000.)
    plot(cPVRes,"TTbar-PVRes-LogY")
if TTSL:
    pvResFH.GetYaxis().SetRangeUser(3.,70000.)
    plot(cPVRes,"TTSL-PVRes-LogY")
if ZP:
    plot(cPVRes,"ZPMM-PVRes-LogY")
if DarkSUSY:
    pvResFH.GetYaxis().SetRangeUser(80.,4000.)
    plot(cPVRes,"DarkSUSY-PVRes-LogY")

pvResFH.GetXaxis().SetRangeUser(-15.,15.)
pvResFH.Rebin(4)
# pvResNNEmu.Rebin(4)
pvResFHEmu.Rebin(4)

if DY:
    pvResFH.GetYaxis().SetRangeUser(1.,100000.)
    plot(cPVRes,"DY-PVRes-LogY-ZoomOut")
if TT:
    pvResFH.GetYaxis().SetRangeUser(1.,50000.)
    plot(cPVRes,"TTbar-PVRes-LogY-ZoomOut")
if TTSL:
    pvResFH.GetYaxis().SetRangeUser(1.,50000.)
    plot(cPVRes,"TTSL-PVRes-LogY-ZoomOut")
if ZP:
    plot(cPVRes,"ZPMM-PVRes-LogY-ZoomOut")
if DarkSUSY:
    pvResFH.GetYaxis().SetRangeUser(1.,14000.)
    plot(cPVRes,"DarkSUSY-PVRes-LogY-ZoomOut")
