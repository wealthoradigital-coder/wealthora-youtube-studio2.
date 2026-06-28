import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit configuration settings
st.set_page_config(page_title="Wealthora Studio Engine", layout="wide")

# 2. Assign the single-file HTML/CSS/JS application code to a string variable
wealthora_studio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wealthora YouTube Studio v4</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');
:root{--navy:#1A1FA8;--navyd:#0d1060;--gold:#E8C800;--white:#fff;--off:#f8f7f2;--g4:#9896be;--g6:#5a5888;--ok:#22c55e;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'DM Sans',sans-serif;background:var(--navyd);color:var(--white);min-height:100vh;}
.hdr{background:linear-gradient(135deg,var(--navyd),var(--navy));border-bottom:2px solid var(--gold);padding:10px 16px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:200;}
.logo{font-family:'Cormorant Garamond',serif;font-size:clamp(16px,4vw,20px);font-weight:700;color:var(--gold);}
.logo span{color:var(--white);font-weight:400;}
.badge{background:var(--gold);color:var(--navyd);font-size:10px;font-weight:700;padding:3px 9px;border-radius:20px;}
.stepper{display:grid;grid-template-columns:1fr 32px 1fr 32px 1fr;align-items:center;padding:12px 16px;background:var(--navyd);border-bottom:1px solid rgba(232,200,0,.15);gap:4px;}
.si{display:flex;flex-direction:column;align-items:center;cursor:pointer;padding:8px 4px;text-align:center;}
.sc{width:34px;height:34px;border-radius:50%;border:2px solid var(--g6);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:var(--g6);transition:all .3s;margin-bottom:5px;}
.si.active .sc{border-color:var(--gold);color:var(--gold);background:rgba(232,200,0,.12);}
.si.done .sc{border-color:var(--ok);color:var(--navyd);background:var(--ok);}
.sl{display:flex;flex-direction:column;align-items:center;}
.sl .sn{font-size:9px;color:var(--g6);display:block;line-height:1;margin-bottom:2px;text-transform:uppercase;letter-spacing:.4px;}
.si.active .sn{color:var(--gold);}.si.done .sn{color:var(--ok);}
.sl .st{font-size:11px;font-weight:600;color:var(--g4);line-height:1.2;text-align:center;}
.si.active .st{color:var(--white);}.si.done .st{color:var(--off);}
.conn{height:2px;background:var(--g6);transition:background .3s;align-self:center;margin-top:-20px;}
.conn.done{background:var(--ok);}
.main{background:var(--navy);min-height:calc(100vh - 120px);padding:14px;}
.panel{display:none;}.panel.active{display:block;}
.pb{display:inline-flex;align-items:center;gap:6px;background:rgba(232,200,0,.1);border:1px solid rgba(232,200,0,.3);padding:4px 12px;border-radius:20px;font-size:11px;font-weight:600;color:var(--gold);margin-bottom:14px;}
.stitle{font-family:'Cormorant Garamond',serif;font-size:24px;font-weight:700;color:var(--gold);margin-bottom:2px;}
.ssub{font-size:12px;color:var(--g4);margin-bottom:18px;}
.card{background:rgba(255,255,255,.05);border:1px solid rgba(232,200,0,.2);border-radius:12px;padding:14px;margin-bottom:12px;}
.ctitle{font-size:11px;font-weight:700;color:var(--gold);text-transform:uppercase;letter-spacing:.8px;margin-bottom:12px;}
label{display:block;font-size:11px;font-weight:600;color:var(--g4);margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px;}
select,input,textarea{width:100%;background:rgba(255,255,255,.07);border:1px solid rgba(232,200,0,.25);border-radius:8px;padding:9px 12px;color:var(--white);font-family:'DM Sans',sans-serif;font-size:13px;margin-bottom:12px;outline:none;transition:border-color .2s;}
select:focus,input:focus,textarea:focus{border-color:var(--gold);background:rgba(255,255,255,.1);}
select option{background:#12157a;}
textarea{min-height:90px;resize:vertical;}
.btn{display:inline-flex;align-items:center;gap:7px;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;border:none;transition:all .2s;font-family:'DM Sans',sans-serif;}
.btn-gold{background:var(--gold);color:var(--navyd);}.btn-gold:hover{background:#f5d800;transform:translateY(-1px);}
.btn-gold:disabled{opacity:.5;cursor:not-allowed;transform:none;}
.btn-out{background:transparent;color:var(--gold);border:1px solid var(--gold);}
.btn-out:hover{background:rgba(232,200,0,.1);}
.btn-out:disabled{opacity:.5;cursor:not-allowed;}
.btn-next{display:flex;background:linear-gradient(135deg,var(--gold),#f5d800);color:var(--navyd);font-size:14px;font-weight:700;padding:13px 28px;width:100%;justify-content:center;align-items:center;gap:8px;margin-top:8px;border-radius:10px;border:none;cursor:pointer;font-family:'DM Sans',sans-serif;}
.btn-next:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(232,200,0,.3);}
.btn-next:disabled{opacity:.5;cursor:not-allowed;transform:none;}
.btn-sm{padding:7px 12px;font-size:12px;}
.btn-row{display:flex;gap:8px;flex-wrap:wrap;}
.ow{position:relative;}
.ob{background:rgba(0,0,0,.35);border:1px solid rgba(232,200,0,.3);border-radius:10px;padding:42px 16px 16px;font-size:13px;line-height:1.8;color:var(--off);white-space:pre-wrap;min-height:80px;word-break:break-word;max-height:none;height:auto;}
.ob.empty{color:var(--g6);font-style:italic;display:flex;align-items:center;justify-content:center;min-height:60px;padding-top:16px;}
#script-out{min-height:200px;}
.cpbtn{position:absolute;top:8px;right:8px;z-index:10;background:rgba(232,200,0,.15);border:1px solid var(--gold);color:var(--gold);padding:4px 11px;border-radius:6px;font-size:11px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;transition:all .2s;}
.cpbtn:hover{background:rgba(232,200,0,.3);}
.idea-list{display:flex;flex-direction:column;gap:8px;margin-bottom:12px;}
.idea-item{background:rgba(255,255,255,.04);border:1px solid rgba(232,200,0,.15);border-radius:9px;padding:12px 14px;cursor:pointer;transition:all .2s;display:flex;align-items:flex-start;gap:10px;}
.idea-item:hover{border-color:rgba(232,200,0,.4);background:rgba(232,200,0,.05);}
.idea-item.sel{border-color:var(--gold);background:rgba(232,200,0,.1);}
.ichk{width:18px;height:18px;border-radius:50%;border:2px solid var(--g6);flex-shrink:0;margin-top:2px;display:flex;align-items:center;justify-content:center;font-size:10px;transition:all .2s;}
.idea-item.sel .ichk{background:var(--gold);border-color:var(--gold);color:var(--navyd);}
.itxt{font-size:13px;color:var(--off);line-height:1.4;font-weight:500;}
.imeta{font-size:11px;color:var(--g6);margin-top:3px;line-height:1.4;}
.vhigh{color:#4ade80;font-weight:600;}
.vmed{color:var(--gold);font-weight:600;}
.vlow{color:var(--g4);font-weight:600;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media(max-width:600px){.g2{grid-template-columns:1fr;}}
.spin{width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:var(--gold);border-radius:50%;animation:sp .8s linear infinite;display:inline-block;vertical-align:middle;margin-right:6px;}
@keyframes sp{to{transform:rotate(360deg);}}
.al{padding:10px 14px;border-radius:8px;font-size:12px;margin-bottom:12px;line-height:1.5;}
.al-info{background:rgba(26,31,168,.4);border:1px solid rgba(232,200,0,.3);color:var(--off);}
.al-ok{background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:#4ade80;}
.al-warn{background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.3);color:#f87171;}
.fwd{background:rgba(34,197,94,.08);border:1px solid rgba(34,197,94,.25);border-radius:10px;padding:12px 16px;margin-bottom:14px;display:none;align-items:center;gap:10px;}
.fwd.show{display:flex;}
.fwdt{font-size:12px;color:#4ade80;flex:1;line-height:1.4;}
.fwdb{background:var(--ok);color:var(--navyd);border:none;padding:8px 16px;border-radius:7px;font-size:12px;font-weight:700;cursor:pointer;font-family:'DM Sans',sans-serif;white-space:nowrap;}
.ctx{background:rgba(232,200,0,.06);border:1px solid rgba(232,200,0,.15);border-radius:10px;padding:12px 16px;margin-bottom:14px;}
.ctxt{font-size:10px;font-weight:700;color:var(--gold);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px;}
.cpills{display:flex;flex-wrap:wrap;gap:6px;}
.cp{background:rgba(255,255,255,.07);border:1px solid rgba(232,200,0,.2);padding:4px 10px;border-radius:20px;font-size:11px;color:var(--off);}
.cp span{color:var(--gold);font-weight:600;}
.fhint{font-size:11px;color:var(--gold);margin-top:-8px;margin-bottom:12px;padding:8px 12px;background:rgba(232,200,0,.07);border-radius:6px;border-left:3px solid var(--gold);line-height:1.5;}
.stabs{display:flex;gap:0;margin-bottom:16px;border-bottom:2px solid rgba(232,200,0,.15);overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;}
.stabs::-webkit-scrollbar{display:none;}
.stab{padding:10px 16px;font-size:12px;font-weight:600;cursor:pointer;color:var(--g4);border-bottom:2px solid transparent;transition:all .2s;margin-bottom:-2px;white-space:nowrap;flex-shrink:0;user-select:none;}
.stab:hover{color:var(--white);background:rgba(255,255,255,.04);}
.stab.active{color:var(--gold);border-bottom-color:var(--gold);background:rgba(232,200,0,.05);}
.ssection{display:none;}.ssection.active{display:block;}
.tbl{width:100%;border-collapse:collapse;font-size:12px;}
.tbl th{text-align:left;padding:8px 10px;color:var(--gold);font-size:10px;text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid rgba(232,200,0,.2);}
.tbl td{padding:8px 10px;border-bottom:1px solid rgba(255,255,255,.05);color:var(--off);vertical-align:middle;}
.pbar{height:5px;background:rgba(255,255,255,.1);border-radius:4px;overflow:hidden;margin-top:6px;}
.pfill{height:100%;background:
