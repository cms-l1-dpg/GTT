import numpy
import ROOT
from ROOT import *

DY=False
TT=False
ZP=False
### Switch ###
DY=True
# TT=True
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

# def writeCMS(canvas):
#     canvas.cd()


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
f=ROOT.TFile("PVPlots_DY_FHE.root")

cPt = TCanvas("cPt", "cPt", 700, 700)
setCanvas(cPt)
f.cd()
trackPt=f.Get("trackPt")
trackPt.SetTitle("Track p_{T};Track p_{T} [GeV];Number of tracks/GeV")
setStyle(trackPt,1)
trackPt.GetXaxis().SetRangeUser(0.0,20.0)
plot(cPt,"TrackPt")

cEta = TCanvas("cEta", "cEta", 700, 700)
setCanvas(cEta)
f.cd()
trackEta=f.Get("trackEta")
trackEta.SetTitle("Track #eta;Track #eta;Number of tracks")
setStyle(trackEta,1)
trackEtaRebinned=trackEta.Rebin(nEtaBins,'',EtaBins)
trackEtaRebinned.GetXaxis().SetRangeUser(-2.6,2.6)
trackEtaRebinned.Draw("ep")
plot(cEta,"trackEta")

cPhi = TCanvas("cPhi", "cPhi", 700, 700)
setCanvas(cPhi)
f.cd()
trackPhi=f.Get("trackPhi")
trackPhi.SetTitle("Track #phi;Track #phi;Number of tracks")
setStyle(trackPhi,1)
trackPhi.Rebin(41)
# trackPhiRebinned=trackPhi.Rebin(nPhiBins,'',PhiBins)
trackPhi.GetXaxis().SetRangeUser(-3.4,3.4)
trackPhi.Draw("ep")
plot(cPhi,"TrackPhi")

cMVA = TCanvas("cMVA", "cMVA", 700, 700)
setCanvas(cMVA)
f.cd()
trackMVA=f.Get("trackMVA")
trackMVA.SetTitle("Track MVA;Track MVA;Number of tracks")
setStyle(trackMVA,1)
# trackMVA.Rebin(41)
# trackMVARebinned=trackMVA.Rebin(nMVABins,'',MVABins)
# trackMVA.GetXaxis().SetRangeUser(-3.4,3.4)
trackMVA.Draw("ep")
plot(cMVA,"TrackMVA")

cTrkFakeFH = TCanvas("cTrkFakeFH", "cTrkFakeFH", 700, 700)
setCanvas(cTrkFakeFH)
f.cd()
trackFakeFH=fFH.Get("trackFake")
trackFakeFH.SetTitle("Track Fakes;Fake Quality;Number of tracks")
setStyle(trackFakeFH,1)
trackFakeFH.Draw("")
plot(cTrkFakeFH,"TrackFakes")
