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
.spin{width:13px;height:13px;border:2px solid rgba(26,31,168,.4);border-top-color:var(--navyd);border-radius:50%;animation:sp .8s linear infinite;display:inline-block;}
@keyframes sp{to{transform:rotate(360deg);}}
.al{padding:10px 14px;border-radius:8px;font-size:12px;margin-bottom:12px;line-height:1.5;}
.al-info{background:rgba(26,31,168,.4);border:1px solid rgba(232,200,0,.3);color:var(--off);}
.al-ok{background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:#4ade80;}
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
.pfill{height:100%;background:var(--gold);border-radius:4px;transition:width .5s;}
.chklist{display:flex;flex-direction:column;gap:7px;}
.chi{display:flex;align-items:center;gap:10px;padding:8px 12px;background:rgba(255,255,255,.04);border-radius:8px;cursor:pointer;}
.chi input[type=checkbox]{width:15px;height:15px;accent-color:var(--gold);cursor:pointer;flex-shrink:0;}
.chi label{margin:0;text-transform:none;letter-spacing:0;font-size:12px;color:var(--off);cursor:pointer;font-weight:400;}
.chi.ticked label{text-decoration:line-through;color:var(--g6);}
.steps{display:flex;flex-direction:column;gap:10px;margin-bottom:12px;}
.step{display:flex;gap:12px;align-items:flex-start;}
.stepn{width:24px;height:24px;border-radius:50%;background:var(--gold);color:var(--navyd);font-weight:700;font-size:11px;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;}
.stepc h4{font-size:13px;font-weight:600;color:var(--white);margin-bottom:1px;}
.stepc p{font-size:11px;color:var(--g4);line-height:1.5;}
.tgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px;}
.tc{background:rgba(255,255,255,.05);border:1px solid rgba(232,200,0,.2);border-radius:10px;padding:13px;cursor:pointer;transition:all .2s;}
.tc:hover{border-color:var(--gold);transform:translateY(-2px);}
.tn{font-size:13px;font-weight:600;color:var(--white);margin-bottom:2px;}
.td2{font-size:11px;color:var(--g4);}
.tc2{font-size:10px;color:var(--gold);margin-top:4px;font-weight:700;}
.vgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px;}
.vc{background:rgba(255,255,255,.05);border:1px solid rgba(232,200,0,.15);border-radius:10px;padding:13px;}
.vc.rec{border-color:var(--gold);background:rgba(232,200,0,.07);}
.vn{font-size:14px;font-weight:700;color:var(--white);margin-bottom:3px;}
.vb{font-size:10px;font-weight:600;padding:2px 7px;border-radius:20px;display:inline-block;margin-bottom:7px;}
.vb.r{background:var(--gold);color:var(--navyd);}
.vb.a{background:rgba(255,255,255,.1);color:var(--g4);}
.vd{font-size:11px;color:var(--g4);line-height:1.5;}
.wc{font-size:11px;color:var(--g4);font-weight:400;text-transform:none;letter-spacing:0;margin-left:8px;}
.pnav{display:flex;gap:10px;margin-top:20px;padding-top:14px;border-top:1px solid rgba(232,200,0,.1);}
.pbk{background:transparent;color:var(--g4);border:1px solid var(--g6);padding:10px 18px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;}
.pbk:hover{color:var(--white);border-color:var(--white);}
.funnel{display:flex;flex-direction:column;align-items:center;text-align:center;}
.fl{border-radius:8px;padding:10px 16px;width:100%;font-size:12px;font-weight:600;}
.farr{font-size:16px;color:var(--g6);padding:3px;line-height:1;}
.flab{font-size:10px;color:var(--g4);margin-bottom:3px;}
#toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(80px);background:var(--navy);border:1px solid var(--gold);color:var(--white);padding:10px 20px;border-radius:10px;font-size:12px;font-weight:600;z-index:9999;transition:transform .3s;pointer-events:none;max-width:90vw;text-align:center;}
#toast.show{transform:translateX(-50%) translateY(0);}
</style>
</head>
<body>
<div id="toast"></div>
<div class="hdr">
  <div class="logo">Wealthora <span>YouTube Studio</span></div>
  <span class="badge">v4 3-PHASE</span>
</div>
<div class="stepper">
  <div class="si active" onclick="goTo(0)" id="si0"><div class="sc" id="sc0">1</div><div class="sl"><span class="sn">PHASE 1</span><span class="st">Ideas &amp; Setup</span></div></div>
  <div class="conn" id="cn0"></div>
  <div class="si" onclick="goTo(1)" id="si1"><div class="sc" id="sc1">2</div><div class="sl"><span class="sn">PHASE 2</span><span class="st">Create &amp; Optimise</span></div></div>
  <div class="conn" id="cn1"></div>
  <div class="si" onclick="goTo(2)" id="si2"><div class="sc" id="sc2">3</div><div class="sl"><span class="sn">PHASE 3</span><span class="st">Publish &amp; Track</span></div></div>
</div>
<div class="main">
<div class="panel active" id="p0">
  <div class="pb">PHASE 1 - Ideas &amp; Setup</div>
  <div class="stitle">Set Up Your Video</div>
  <div class="ssub">Configure once - everything flows forward automatically into Phase 2 and 3</div>
  <div class="card">
    <div class="ctitle">Video Configuration</div>
    <div class="g2">
      <div>
        <label>Product to Promote</label>
        <select id="s-product">
          <option value="agency">Agency Performance Stack</option>
          <option value="realestate">Real Estate Content Matrix</option>
          <option value="fatigue">Digital Fatigue Reset</option>
          <option value="intentiq">IntentIQ</option>
          <option value="bizbox">BizBox AI Pro</option>
        </select>
      </div>
      <div>
        <label>Video Type</label>
        <select id="s-style" onchange="onStyleChange()">
          <option value="educational">Educational / How-To</option>
          <option value="listicle">Listicle (Top 5, 7 Ways)</option>
          <option value="story">Story / Case Study</option>
          <option value="mistake">Common Mistakes</option>
          <option value="controversial">Hot Take / Controversial</option>
          <option value="flywheel">FLYWHEEL Masterclass (45-60 min)</option>
          <option value="shorts">YouTube Short (60 sec)</option>
        </select>
        <div id="style-hint" class="fhint" style="display:none;"></div>
      </div>
    </div>
    <div class="g2">
      <div>
        <label>Script Formula</label>
        <select id="s-formula" onchange="onFormulaChange()">
          <option value="ppb">PPB - Problem, Promise, Bridge</option>
          <option value="aida">AIDA - Attention, Interest, Desire, Action</option>
          <option value="pas">PAS - Problem, Agitate, Solve</option>
          <option value="bab">BAB - Before, After, Bridge</option>
          <option value="storysell">Story-Sell - Open loop narrative</option>
          <option value="listicle">Listicle - Countdown tension</option>
          <option value="myth">Myth-Busting - Instant authority</option>
          <option value="qab">Question-Answer Bridge</option>
          <option value="case">Case Study - Highest trust</option>
          <option value="todd">Value Ladder - Reciprocity engine</option>
        </select>
        <div id="formula-hint" class="fhint" style="display:none;"></div>
      </div>
      <div>
        <label>Tone of Voice</label>
        <select id="s-tone">
          <option value="authoritative">Authoritative Expert</option>
          <option value="conversational">Conversational Friend</option>
          <option value="urgent">Urgent Warning</option>
          <option value="motivational">Motivational Coach</option>
          <option value="controversial">Controversial Challenger</option>
        </select>
        <label>Video Length</label>
        <select id="s-length">
          <option value="shorts">Short (60 sec)</option>
          <option value="short">Short (5-7 mins)</option>
          <option value="medium" selected>Medium (8-12 mins)</option>
          <option value="long">Long (15-20 mins)</option>
          <option value="flywheel">Flywheel Masterclass (45-60 mins)</option>
        </select>
      </div>
    </div>
    <button class="btn btn-gold" id="gen-ideas-btn" onclick="generateIdeas()">Generate 10 Video Ideas</button>
  </div>
  <div class="card" id="idea-card" style="display:none;">
    <div class="ctitle">Video Ideas - Ranked Highest to Lowest Viral</div>
    <div class="al al-ok">Top Pick auto-selected. Key points auto-fill when you tap any idea. Edit before continuing.</div>
    <div class="idea-list" id="idea-list"></div>
    <label>Or type a custom title</label>
    <input type="text" id="custom-title" placeholder="Type your own video title..."/>
    <label>Key Points <span style="color:#22c55e;font-size:10px;font-weight:600;text-transform:none;letter-spacing:0;margin-left:6px;">Auto-filled - edit if needed</span></label>
    <textarea id="key-points" placeholder="Select an idea above - key points auto-populate&#10;&#10;Or type your own:&#10;- Pain point 1&#10;- Pain point 2&#10;- CTA"></textarea>
    <button class="btn-next" id="proceed-btn" onclick="proceedToPhase2()">Generate Script, SEO, Thumbnail and Description</button>
  </div>
  <div class="card">
    <div class="ctitle">Beginner Fast-Start Roadmap</div>
    <div class="steps">
      <div class="step"><div class="stepn">W1</div><div class="stepc"><h4>Weeks 1-2 - Brand Assets</h4><p>Set up HeyGen AI avatar, ElevenLabs Daniel voice, Canva gold-on-navy templates.</p></div></div>
      <div class="step"><div class="stepn">W3</div><div class="stepc"><h4>Week 3 - Build Flywheel Masterclass FIRST</h4><p>Create 45-60 min masterclass. Upload it before any short videos. This is your 24/7 sales engine.</p></div></div>
      <div class="step"><div class="stepn">W4</div><div class="stepc"><h4>Week 4+ - Regular 8-12 Min Traffic Videos</h4><p>Post 2 searchable videos per week. Every end screen points to your Flywheel Masterclass.</p></div></div>
    </div>
    <div style="margin-top:12px;padding:10px 14px;background:rgba(232,200,0,.07);border:1px solid rgba(232,200,0,.2);border-radius:8px;font-size:12px;color:var(--gold);">Flywheel Formula: Short video - End screen - Masterclass - Email capture - Product sale</div>
  </div>
  <div class="card">
    <div class="ctitle">Affiliate Revenue Stack</div>
    <table class="tbl">
      <thead><tr><th>Tool</th><th>Commission</th><th>Use In</th></tr></thead>
      <tbody>
        <tr><td>ElevenLabs</td><td style="color:#4ade80;">Recurring monthly</td><td>AI voice videos</td></tr>
        <tr><td>Canva Pro</td><td style="color:#4ade80;">Recurring monthly</td><td>Design videos</td></tr>
        <tr><td>HeyGen</td><td style="color:#4ade80;">Recurring monthly</td><td>AI avatar videos</td></tr>
        <tr><td>Selar</td><td style="color:var(--gold);">Per sale</td><td>Digital product videos</td></tr>
        <tr><td>CapCut Pro</td><td style="color:var(--gold);">Per referral</td><td>Editing videos</td></tr>
      </tbody>
    </table>
  </div>
</div>
<div class="panel" id="p1">
  <div class="pb">PHASE 2 - Create and Optimise</div>
  <div class="stitle">All Content Generated</div>
  <div class="ssub">Script, SEO, Thumbnail Brief and Description - all in one phase</div>
  <div class="ctx"><div class="ctxt">Carried from Phase 1</div><div class="cpills" id="ctx-pills"></div></div>
  <div class="fwd" id="fwd-banner"><div class="fwdt">Everything generated - review each section, copy what you need, then go to Phase 3</div><button class="fwdb" onclick="goTo(2)">Go to Phase 3</button></div>
  <div class="stabs">
    <div class="stab active" onclick="showSec('sec-script',this)">Script</div>
    <div class="stab" onclick="showSec('sec-seo',this)">SEO</div>
    <div class="stab" onclick="showSec('sec-thumb',this)">Thumbnail</div>
    <div class="stab" onclick="showSec('sec-desc',this)">Description</div>
  </div>
  <div class="ssection active" id="sec-script">
    <div class="card">
      <div class="ctitle">Full Script <span class="wc" id="wc-display"></span></div>
      <div class="btn-row" style="margin-bottom:12px;">
        <button class="btn btn-gold btn-sm" id="regen-script-btn" onclick="regenScript()">Regenerate Script</button>
        <button class="btn btn-out btn-sm" id="regen-hook-btn" onclick="regenHook()">New Hooks</button>
        <button class="btn btn-out btn-sm" id="regen-cta-btn" onclick="regenCTA()">New CTAs</button>
        <button class="btn btn-out btn-sm" onclick="downloadScript()">Download .txt</button>
      </div>
      <div class="ow"><button class="cpbtn" onclick="cpOut('script-out',this)">Copy</button><div class="ob empty" id="script-out">Click Generate in Phase 1 to create your script...</div></div>
    </div>
    <div class="card" id="hook-card" style="display:none;">
      <div class="ctitle">Alternative Hooks</div>
      <div class="ow"><button class="cpbtn" onclick="cpOut('hook-out',this)">Copy</button><div class="ob empty" id="hook-out"></div></div>
    </div>
    <div class="card" id="cta-card" style="display:none;">
      <div class="ctitle">Alternative CTAs</div>
      <div class="ow"><button class="cpbtn" onclick="cpOut('cta-out',this)">Copy</button><div class="ob empty" id="cta-out"></div></div>
    </div>
  </div>
  <div class="ssection" id="sec-seo">
    <div class="card"><div class="ctitle">SEO Package - Titles, Tags, Keywords, Chapters</div><div class="ow"><button class="cpbtn" onclick="cpOut('seo-out',this)">Copy</button><div class="ob empty" id="seo-out">SEO package will appear here...</div></div></div>
  </div>
  <div class="ssection" id="sec-thumb">
    <div class="card"><div class="ctitle">Canva Thumbnail Brief</div><div class="al al-info">Open Canva alongside this brief. Follow each section in order. Target: 15 minutes to build.</div><div class="ow"><button class="cpbtn" onclick="cpOut('thumb-out',this)">Copy</button><div class="ob empty" id="thumb-out">Thumbnail brief will appear here...</div></div></div>
  </div>
  <div class="ssection" id="sec-desc">
    <div class="card"><div class="ctitle">YouTube Description</div><div class="al al-info">Before uploading: replace Flywheel URL placeholder and affiliate link placeholders with your actual links.</div><div class="ow"><button class="cpbtn" onclick="cpOut('desc-out',this)">Copy</button><div class="ob empty" id="desc-out">Description will appear here...</div></div></div>
  </div>
  <div class="pnav">
    <button class="pbk" onclick="goTo(0)">Back to Phase 1</button>
    <button class="btn-next" style="flex:1;" onclick="goTo(2)">Continue to Publish and Track</button>
  </div>
</div>
<div class="panel" id="p2">
  <div class="pb">PHASE 3 - Publish and Track</div>
  <div class="stitle">Production, Upload and Analytics</div>
  <div class="ssub">Everything you need to produce, upload, and track your video</div>
  <div class="ctx"><div class="ctxt">Your Video</div><div class="cpills" id="ctx-pills-3"></div></div>
  <div class="stabs">
    <div class="stab active" onclick="showSec('sec-prod',this)">Production</div>
    <div class="stab" onclick="showSec('sec-upload',this)">Upload</div>
    <div class="stab" onclick="showSec('sec-tracker',this)">Tracker</div>
    <div class="stab" onclick="showSec('sec-analytics',this)">Analytics</div>
  </div>
  <div class="ssection active" id="sec-prod">
    <div class="card">
      <div class="ctitle">Step 1 - Voiceover on ElevenLabs</div>
      <div class="vgrid">
        <div class="vc rec"><div class="vn">Daniel</div><span class="vb r">RECOMMENDED</span><div class="vd">British, deep, authoritative. Perfect for Alexander E. Reid brand.</div><div style="margin-top:6px;font-size:10px;color:var(--gold);">Stability 65% | Similarity 80% | Style 0%</div></div>
        <div class="vc"><div class="vn">Adam</div><span class="vb a">ALTERNATIVE</span><div class="vd">Deep American. High energy business content.</div></div>
        <div class="vc"><div class="vn">Antoni</div><span class="vb a">ALTERNATIVE</span><div class="vd">Warm, clear. Best for educational tutorials.</div></div>
        <div class="vc"><div class="vn">Josh</div><span class="vb a">ALTERNATIVE</span><div class="vd">Engaging, relatable. Best for storytelling.</div></div>
      </div>
    </div>
    <div class="card">
      <div class="ctitle">Step 2 - B-Roll Footage (Free)</div>
      <div class="tgrid">
        <div class="tc" onclick="window.open('https://pexels.com/videos','_blank')"><div class="tn">Pexels</div><div class="td2">Best free stock footage</div><div class="tc2">FREE</div></div>
        <div class="tc" onclick="window.open('https://pixabay.com/videos','_blank')"><div class="tn">Pixabay</div><div class="td2">Great for tech content</div><div class="tc2">FREE</div></div>
        <div class="tc" onclick="window.open('https://coverr.co','_blank')"><div class="tn">Coverr</div><div class="td2">Premium-looking clips</div><div class="tc2">FREE</div></div>
        <div class="tc" onclick="window.open('https://mixkit.co','_blank')"><div class="tn">Mixkit</div><div class="td2">Footage plus free music</div><div class="tc2">FREE</div></div>
      </div>
    </div>
    <div class="card">
      <div class="ctitle">Step 3 - Edit in CapCut</div>
      <div class="steps">
        <div class="step"><div class="stepn">1</div><div class="stepc"><h4>New Project 1920x1080</h4><p>Import all MP3 sections, arrange on timeline in order.</p></div></div>
        <div class="step"><div class="stepn">2</div><div class="stepc"><h4>Add B-Roll</h4><p>Import clips, place on video track above each audio section.</p></div></div>
        <div class="step"><div class="stepn">3</div><div class="stepc"><h4>Auto-Captions</h4><p>Text, Auto Caption, English. Style: white bold, navy outline. Review every line.</p></div></div>
        <div class="step"><div class="stepn">4</div><div class="stepc"><h4>Background Music</h4><p>Audio, Music, Corporate or Inspiring. Volume: exactly 12%. Never higher.</p></div></div>
        <div class="step"><div class="stepn">5</div><div class="stepc"><h4>Export</h4><p>1080p, 30fps, H.264. File under 2GB.</p></div></div>
      </div>
    </div>
    <div class="card">
      <div class="ctitle">Pre-Upload Copyright Checklist</div>
      <div class="chklist">
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>All footage from Pexels, Pixabay, Coverr or Mixkit only</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Background music from CapCut library or Mixkit only - no popular songs</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Script is 100% original - not copied from another video</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>No TV, movie or news clips used</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Thumbnail does not use celebrity faces or trademarked logos</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Exported at 1080p / 30fps / H.264</label></div>
      </div>
    </div>
  </div>
  <div class="ssection" id="sec-upload">
    <div class="card">
      <div class="ctitle">YouTube Upload Checklist</div>
      <div class="chklist">
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Title - paste starred title from Phase 2 SEO output</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Description - paste full description (replace Flywheel URL and affiliate link placeholders)</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Tags - paste all 30 tags from SEO output</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Chapters - paste timestamps from SEO output into description</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Thumbnail - upload Canva PNG file</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Category - Education | Language - English</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Set End Screen pointing to Flywheel Masterclass video (CRITICAL)</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Schedule for 9AM Wednesday or Saturday</label></div>
      </div>
    </div>
    <div class="card">
      <div class="ctitle">First 48 Hours - Do These Immediately After Publishing</div>
      <div class="chklist">
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Pin your product link as the first comment</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Post video link on WhatsApp status</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Post 60-second clip on Instagram Reels</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Reply to every comment within 2 hours</label></div>
        <div class="chi" onclick="tc(this)"><input type="checkbox"><label>Verify end screen is showing correctly on mobile</label></div>
      </div>
    </div>
    <div style="margin-top:14px;"><button class="btn btn-gold" style="width:100%;justify-content:center;padding:13px;" onclick="markPublished()">Mark as Published - Update Tracker</button></div>
  </div>
  <div class="ssection" id="sec-tracker">
    <div class="card"><div class="ctitle">Pipeline - <span id="vid-count" style="color:var(--white);font-weight:400;text-transform:none;letter-spacing:0;">0 videos</span></div><div style="overflow-x:auto;"><table class="tbl"><thead><tr><th>Title</th><th>Product</th><th>Status</th><th>Date</th><th></th></tr></thead><tbody id="tbody"></tbody></table></div></div>
    <div class="card"><div class="ctitle">Monthly Goal</div><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;"><span style="font-size:12px;color:var(--g4);">Published this month</span><span style="font-size:13px;font-weight:700;" id="m-count">0 / 8 target</span></div><div class="pbar"><div class="pfill" id="m-bar" style="width:0%"></div></div><div style="margin-top:8px;font-size:11px;color:var(--g4);">2 videos/week = 8/month | Post Wednesday and Saturday at 9AM</div></div>
    <div class="card"><div class="ctitle">Flywheel Funnel</div><div class="funnel"><div class="fl" style="background:rgba(232,200,0,.1);border:1px solid rgba(232,200,0,.3);color:var(--gold);">Searchable 8-12 Min Videos (2 per week)</div><div class="farr">v</div><div class="flab">End Screen drives to</div><div class="fl" style="background:rgba(232,200,0,.2);border:2px solid var(--gold);color:var(--gold);font-weight:700;">Flywheel Masterclass (45-60 min - 24/7 sales engine)</div><div class="farr">v</div><div class="flab">Description Link 2 drives to</div><div class="fl" style="background:rgba(96,165,250,.1);border:1px solid rgba(96,165,250,.3);color:#93c5fd;">Free Scorecard Bridge Page (email capture)</div><div class="farr">v</div><div class="fl" style="background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:#4ade80;">Email Sequence - Product Sales</div></div></div>
    <div style="margin-top:14px;"><button class="btn-next" onclick="newVideo()">Start New Video</button></div>
  </div>
  <div class="ssection" id="sec-analytics">
    <div class="card"><div class="ctitle">Key Benchmarks</div><table class="tbl"><thead><tr><th>Metric</th><th>Poor</th><th>Average</th><th>Good</th></tr></thead><tbody><tr><td>CTR</td><td style="color:#f87171;">&lt;2%</td><td style="color:var(--gold);">2-4%</td><td style="color:#4ade80;">4-8%+</td></tr><tr><td>Retention</td><td style="color:#f87171;">&lt;30%</td><td style="color:var(--gold);">30-50%</td><td style="color:#4ade80;">50%+</td></tr><tr><td>Sub/View</td><td style="color:#f87171;">&lt;0.5%</td><td style="color:var(--gold);">0.5-2%</td><td style="color:#4ade80;">2%+</td></tr></tbody></table></div>
    <div class="card"><div class="ctitle">Sunday Analytics Checklist</div><div class="chklist"><div class="chi" onclick="tc(this)"><input type="checkbox"><label>CTR below 3%? Replace thumbnail this week</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Check retention graph - where do viewers drop off?</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Top performing video this week - make a follow-up next</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Read all comments - 3 questions become next video ideas</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Flywheel Masterclass views growing from end screens?</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Email list growth from YouTube this week?</label></div><div class="chi" onclick="tc(this)"><input type="checkbox"><label>Reply to all comments from the week</label></div></div></div>
    <div class="card"><div class="ctitle">AI Analytics Advisor</div><label>Describe Your Analytics Problem</label><textarea id="analytics-in" placeholder="e.g. My videos get 200 views but only 2 subscribers. CTR is 2.1%. Most viewers drop off at 3 minutes..."></textarea><button class="btn btn-gold" id="analytics-btn" onclick="analyzeAnalytics()">Get AI Diagnosis</button><br><br><div class="ow"><button class="cpbtn" onclick="cpOut('analytics-out',this)">Copy</button><div class="ob empty" id="analytics-out">Your diagnosis will appear here...</div></div></div>
  </div>
  <div class="pnav"><button class="pbk" onclick="goTo(1)">Back to Phase 2</button><button class="btn-next" style="flex:1;" onclick="newVideo()">Start New Video</button></div>
</div>
</div>
<script>
var P={
  agency:{name:'Agency Performance Stack',audience:'Nigerian digital agency owners',pain:'struggling to scale, losing clients, and not making enough profit',cta:'Download the FREE Agency Performance Scorecard at agencyscorecard1.netlify.app',link:'agencyscorecard1.netlify.app',topics:['agency growth Nigeria','client management','AI for agencies','pricing strategy','Nigerian digital agencies']},
  realestate:{name:'Real Estate Content Matrix',audience:'Nigerian real estate agents in Lagos and Abuja',pain:'not knowing what to post on social media and losing clients to competitors',cta:'Grab the Real Estate Content Matrix on Selar - AI content system for Nigerian agents',link:'selar.co',topics:['real estate Nigeria','Lagos property','real estate content','agent marketing Nigeria']},
  fatigue:{name:'Digital Fatigue Reset',audience:'Nigerian remote workers and digital freelancers',pain:'screen burnout, constant exhaustion, and inability to focus after long work sessions',cta:'Get the Digital Fatigue Reset on Selar - your 7-day screen worker recovery protocol',link:'selar.co',topics:['digital fatigue','screen burnout','remote work Nigeria','productivity Nigeria']},
  intentiq:{name:'IntentIQ',audience:'Nigerian social media managers and digital marketers',pain:'not knowing which followers actually want to buy versus those who just scroll',cta:'Access IntentIQ - the only social intent tracker built for the Nigerian market',link:'whogohost.com',topics:['social media Nigeria','intent tracking','Nigerian marketing','Instagram Nigeria']},
  bizbox:{name:'BizBox AI Pro',audience:'Nigerian small business owners and entrepreneurs',pain:'juggling too many apps and having no central system to run their business',cta:'Get BizBox AI Pro - the all-in-one AI business OS for Nigerian entrepreneurs',link:'netlify.app',topics:['Nigerian business','small business Nigeria','business automation Nigeria','entrepreneur Nigeria']}
};
var TONES={
  authoritative:'Authoritative Expert - confident, precise. Voice of Alexander E. Reid, agency growth strategist.',
  conversational:'Conversational Friend - warm, relatable, casual but credible. Like advice from a smart friend in Lagos.',
  urgent:'Urgent Warning - high stakes, alarming. The viewer needs to act NOW.',
  motivational:'Motivational Coach - inspiring, empowering, belief-building.',
  controversial:'Controversial Challenger - bold, provocative, challenges Nigerian industry norms.'
};
var LENGTHS={
  shorts:'60-second YouTube Short (150-180 words, ultra punchy)',
  short:'5-7 minute (800-1000 words)',
  medium:'8-12 minute (1500-1800 words)',
  long:'15-20 minute (2500-3000 words)',
  flywheel:'45-60 minute Flywheel Masterclass (deliver massive value for 85%, product pitch in final 15%)'
};
var FDESCS={
  ppb:'PPB: Make viewer feel the pain, promise transformation, show exactly how. Highest retention for business content.',
  aida:'AIDA: Shock, build context, create desire, drive action. Classic direct-response. Best for product launch videos.',
  pas:'PAS: Name pain, twist the knife, deliver relief. Highest emotional urgency. Best for pain-point heavy topics.',
  bab:'BAB: Paint the painful now, show the desired future, explain how to get there. Powerful for transformation content.',
  storysell:'Story-Sell: Open mid-story, hold tension throughout, resolve while weaving in the product. Netflix style.',
  listicle:'Listicle: Promise X things upfront, count down with tension, build to the best point last. Highest completion rate.',
  myth:'Myth-Busting: State a belief, destroy it with evidence, replace with truth. Creates instant authority.',
  qab:'Question-Answer Bridge: Structure content as questions the viewer is internally asking. Feels like a conversation.',
  case:'Case Study: Open with the result, walk through exact steps, extract repeatable framework. Highest trust builder.',
  todd:'Value Ladder: Deliver a quick win in first 60 seconds, layer deeper value, soft-sell at 70% mark.'
};
var STYLE_HINTS={
  educational:'Standard content video. Best for search traffic. Post 2 per week from Week 4 onwards.',
  listicle:'High completion rate. Works well for beginners. Easy to script and edit.',
  story:'Builds deep trust. Best for case study and transformation content.',
  mistake:'Pain-point driven. High shares. Great for Nigerian business audience.',
  controversial:'High engagement. Use sparingly - 1 in every 5 videos maximum.',
  flywheel:'BUILD THIS FIRST in Week 3. This is your 24/7 sales engine. Every short video points back to this. App will auto-set formula to Value Ladder.',
  shorts:'Post Shorts by extracting 60-second clips from your long videos.'
};
var BLUEPRINTS={
  ppb:'FORMULA: PPB (Problem-Promise-Bridge)\n[HOOK 0:00-0:30] Make the viewer FEEL the problem viscerally. Specific. No greetings. Drop straight into the pain.\n[PROMISE 0:30-1:00] Make ONE bold specific believable promise. Tell them the exact transformation by end of video.\n[BRIDGE INTRO 1:00-1:30] Who you are (1 sentence), why you are qualified, what the bridge looks like.\n[BRIDGE CONTENT 1:30+] 4-5 steps. Each: subheading + full narration + Nigerian example/naira amount + B-ROLL note + micro-payoff.\n[PATTERN INTERRUPT midpoint] Bold question or shocking local statistic.\n[PROOF POINT] One specific Nigerian result that proves the bridge works.\n[CTA 70% mark] Natural bridge to offer.\n[OUTRO] Tease next video. Subscribe ask.',
  aida:'FORMULA: AIDA (Attention-Interest-Desire-Action)\n[ATTENTION 0:00-0:30] One sentence that stops the scroll. Shocking stat or bold claim.\n[INTEREST 0:30-2:00] Why this matters, why now, why listen to you. Nigerian market data.\n[DESIRE 2:00-7:00] Paint Before vs After vividly. Use story, social proof, specificity.\n[PATTERN INTERRUPT midpoint] Direct question. Break fourth wall.\n[ACTION 7:00-8:00] Clear numbered action steps.\n[CTA 70% mark] Deliver CTA as the logical next step.\n[OUTRO] Reinforce transformation. Subscribe with a specific reason.',
  pas:'FORMULA: PAS (Problem-Agitate-Solve)\n[PROBLEM 0:00-0:45] Name the EXACT problem surgically. Specific painful Nigerian situation.\n[AGITATE 0:45-3:00] Twist the knife. Stack the consequences. Cost in naira, time, missed opportunities. Do NOT offer hope yet.\n[PATTERN INTERRUPT midpoint] But here is what almost nobody in Nigeria is talking about...\n[SOLVE 3:00-8:00] Deliver relief. Each solution directly answers one aspect of the agitated problem. Nigerian example per point.\n[PROOF] One specific Nigerian result.\n[CTA 70% mark] The fastest way to implement everything I just showed you is...\n[OUTRO] Future-pace their life after the solve.',
  bab:'FORMULA: BAB (Before-After-Bridge)\n[BEFORE 0:00-1:30] Paint current painful reality vividly. Nigerian context, naira amounts.\n[PATTERN INTERRUPT] But what if this entire situation could change in 30 days?\n[AFTER 1:30-3:00] Paint desired future with equal vividness. Make it REAL and ACHIEVABLE.\n[BRIDGE 3:00-8:00] Exactly how to get from Before to After. 4-5 steps. Each: label + narration + Nigerian example + B-ROLL note.\n[PROOF midpoint] Real Before/After example that proves the Bridge works.\n[CTA 70% mark] The Bridge I gave you is the framework. The tool that makes it 10x faster is...\n[OUTRO] Remind them of the After. Tease next video.',
  storysell:'FORMULA: STORY-SELL (Open Loop Narrative)\n[OPEN LOOP HOOK 0:00-0:45] Open MID-STORY. Drop viewer into a specific moment of crisis or discovery. Example: It was a Tuesday in Lagos when I realised everything I had been taught was wrong...\n[CONTEXT BRIDGE 0:45-1:30] Brief context. Who, what, why it matters. Promise the story resolution comes - but first, here is what you need to understand.\n[STORY-DRIVEN CONTENT 1:30-7:00] Each content point revealed through the story. Maintain the open loop. B-ROLL notes throughout.\n[PATTERN INTERRUPT midpoint] Return to open loop story with a new development.\n[STORY RESOLUTION + CTA 70% mark] CLOSE THE LOOP. Resolution leads naturally into product.\n[OUTRO] Start a NEW open loop for next video.',
  listicle:'FORMULA: LISTICLE (Countdown Tension)\n[HOOK 0:00-0:30] State the number and promise: There are X reasons Nigerian audience will fail/succeed in 2026. Number X will change how you think about this topic forever.\n[CREDIBILITY 0:30-1:00] One sentence on why you can speak on this. Move fast.\n[THE LIST 1:00-8:00] Each item: NUMBER LABEL + TITLE | Full narration | Nigerian naira context | B-ROLL note | Mini-payoff | TEASE next point.\n[PATTERN INTERRUPT midpoint] Before I give you number X - I need to say something most channels will not tell you...\n[CTA 70% mark - BETWEEN two items] Natural CTA placement then return to finish list.\n[OUTRO] Recap in one sentence. Tease follow-up list.',
  myth:'FORMULA: MYTH-BUSTING\n[HOOK 0:00-0:30] State a widely believed myth then challenge it: Everyone in Nigerian digital space tells you X. They are wrong. It is costing you Y.\n[MYTH SETUP 0:30-1:00] Acknowledge why the myth exists. Shows empathy.\n[MYTH 1 BUST 1:00-3:00] THE MYTH | WHY PEOPLE BELIEVE IT | THE TRUTH | THE COST | THE REPLACEMENT BELIEF\n[MYTH 2 BUST 3:00-5:30] Same structure. More surprising than Myth 1.\n[PATTERN INTERRUPT midpoint] The next myth I am about to bust - I believed myself for 2 years.\n[MYTH 3 BUST 5:30-7:30] Most powerful myth. The one that will get shared.\n[TRUTH FRAMEWORK 7:30-8:00] The correct framework. 3-4 sentences.\n[CTA 70% mark]\n[OUTRO] Challenge them to share with one Nigerian business owner still believing the myths.',
  qab:'FORMULA: QUESTION-ANSWER BRIDGE\n[HOOK QUESTION 0:00-0:30] Open with THE ONE question your audience is secretly asking. Specific, vulnerable, real.\n[PERMISSION BRIDGE 0:30-1:00] If you have ever asked yourself that - this video is specifically for you.\n[Q AND A FLOW 1:00-8:00] 4-6 questions building on each other. Q1 then ANSWER then B-ROLL note then BRIDGE: But answering that raises a bigger question... then Q2 etc.\n[PATTERN INTERRUPT midpoint] Most counterintuitive question. Here is what nobody in Nigerian digital space is asking - but should be...\n[MASTER QUESTION 7:00-7:30] Final deepest question. Answer completely.\n[CTA 70% mark] So the only question left is: how do you implement this?\n[OUTRO] Pose one final question. Tease next video as the answer.',
  case:'FORMULA: CASE STUDY\n[RESULT HOOK 0:00-0:30] Open with the RESULT: In X timeframe, person/business went from painful before to specific after. Specific numbers. Relatable before. Aspirational after.\n[CONTEXT 0:30-1:30] Who is this case study? Starting point very relatable to Nigerian audience.\n[TURNING POINT 1:30-2:00] The specific moment or decision that changed everything.\n[STEP-BY-STEP 2:00-7:30] Each step: NUMBER + LABEL | What was done | Why it worked | Nigerian context | B-ROLL note | Result of this step.\n[PATTERN INTERRUPT midpoint] Here is where most people give up - and why our case study did not...\n[FRAMEWORK 7:30-8:00] Pull repeatable framework. Give it a name.\n[CTA 70% mark] I have packaged this exact framework into...\n[OUTRO] Tease follow-up case study.',
  todd:'FORMULA: VALUE LADDER (Todd Beauchamp) - BEST FOR FLYWHEEL MASTERCLASS\n[QUICK WIN HOOK 0:00-1:00] Deliver a COMPLETE USABLE insight in first 60 seconds. Real value. Creates immediate reciprocity.\n[ESCALATION BRIDGE 1:00-1:30] That was surface level. What I am about to show you goes much deeper.\n[VALUE LAYER 1 1:30-3:30] Solid foundational value. Practical. Nigerian context.\n[VALUE LAYER 2 3:30-5:30] Deeper, more sophisticated. Builds on Layer 1.\n[PATTERN INTERRUPT midpoint] Here is what separates the top 10% of Nigerian digital businesses from everyone else...\n[VALUE LAYER 3 5:30-7:00] Premium insight. Something they would pay for.\n[RECIPROCITY CTA 70% mark] I have given you the framework. If you want the complete system...\n[BONUS LAYER 4 7:00-8:00] One more bonus insight AFTER the CTA. Rewards viewers who stayed.\n[OUTRO] Promise next video opens with another quick win.'
};
var S={pk:'agency',title:'',formula:'ppb',tone:'authoritative',length:'medium',style:'educational',kp:''};
var ideas=[];
var selIdx=-1;
var videos=[];
try{videos=JSON.parse(localStorage.getItem('wyd_v4')||'[]');}catch(e){videos=[];}
function goTo(n){
  for(var i=0;i<3;i++){
    document.getElementById('p'+i).classList.toggle('active',i===n);
    var si=document.getElementById('si'+i);
    si.classList.remove('active','done');
    if(i<n){si.classList.add('done');}
    else if(i===n){si.classList.add('active');}
    document.getElementById('sc'+i).textContent=i<n?'v':(i+1);
    if(i<2){document.getElementById('cn'+i).classList.toggle('done',i<n);}
  }
  if(n===1){resetTabs('p1');}
  if(n===2){resetTabs('p2');}
  window.scrollTo({top:0,behavior:'smooth'});
}
function resetTabs(panelId){
  var panel=document.getElementById(panelId);
  var tabs=panel.querySelectorAll('.stab');
  var secs=panel.querySelectorAll('.ssection');
  for(var i=0;i<tabs.length;i++){tabs[i].classList.toggle('active',i===0);}
  for(var i=0;i<secs.length;i++){secs[i].classList.toggle('active',i===0);}
}
function showSec(id,tab){
  var stabs=tab.parentElement;
  var container=stabs.parentElement;
  stabs.querySelectorAll('.stab').forEach(function(t){t.classList.remove('active');});
  tab.classList.add('active');
  container.querySelectorAll('.ssection').forEach(function(s){s.classList.remove('active');});
  var target=document.getElementById(id);
  if(target){target.classList.add('active');}
}
function onFormulaChange(){
  var v=document.getElementById('s-formula').value;
  var el=document.getElementById('formula-hint');
  if(!el)return;
  var text=FDESCS[v]||'';
  el.textContent=text;
  el.style.display=text?'block':'none';
}
function onStyleChange(){
  var v=document.getElementById('s-style').value;
  var el=document.getElementById('style-hint');
  if(el){
    var hint=STYLE_HINTS[v]||'';
    el.textContent=hint;
    el.style.display=hint?'block':'none';
  }
  if(v==='flywheel'){
    document.getElementById('s-formula').value='todd';
    var lenSel=document.getElementById('s-length');
    var hasOpt=false;
    for(var i=0;i<lenSel.options.length;i++){if(lenSel.options[i].value==='flywheel'){hasOpt=true;break;}}
    if(!hasOpt){var opt=document.createElement('option');opt.value='flywheel';opt.text='Flywheel Masterclass (45-60 mins)';lenSel.appendChild(opt);}
    lenSel.value='flywheel';
    onFormulaChange();
    toast('Flywheel mode activated - formula set to Value Ladder');
  }
}
function tc(item){
  var cb=item.querySelector('input[type=checkbox]');
  cb.checked=!cb.checked;
  item.classList.toggle('ticked',cb.checked);
}
function toast(msg){
  var t=document.getElementById('toast');
  t.textContent=msg;
  t.classList.add('show');
  setTimeout(function(){t.classList.remove('show');},2800);
}
function cpOut(id,btn){
  var el=document.getElementById(id);
  if(!el)return;
  var text=el.textContent.trim();
  if(!text||el.classList.contains('empty'))return;
  if(text.length<20)return;
  function doFallback(){
    var ta=document.createElement('textarea');
    ta.value=text;
    ta.style.cssText='position:fixed;left:-9999px;opacity:0;';
    document.body.appendChild(ta);
    ta.select();
    try{document.execCommand('copy');toast('Copied!');}catch(e){}
    document.body.removeChild(ta);
  }
  if(navigator.clipboard&&window.isSecureContext){
    navigator.clipboard.writeText(text).then(function(){toast('Copied!');}).catch(doFallback);
  }else{doFallback();}
}
function setOB(id,txt){
  var el=document.getElementById(id);
  if(!el)return;
  if(txt&&txt.trim()){
    el.classList.remove('empty');
    el.textContent=txt;
    el.style.display='';
  }else{
    el.classList.add('empty');
    el.textContent='Output will appear here...';
  }
}
function setBL(id,loading,orig){
  var b=document.getElementById(id);
  if(!b)return;
  b.disabled=loading;
  b.innerHTML=loading?'<span class="spin"></span> Generating...':orig;
}
function updateCtx(){
  var prod=P[S.pk];
  var fmap={ppb:'PPB',aida:'AIDA',pas:'PAS',bab:'BAB',storysell:'Story-Sell',listicle:'Listicle',myth:'Myth-Bust',qab:'Q-A-B',case:'Case Study',todd:'Value Ladder'};
  var lmap={shorts:'60sec',short:'5-7min',medium:'8-12min',long:'15-20min',flywheel:'Flywheel'};
  var html='<div class="cp"><span>Title:</span> '+(S.title||'Not set')+'</div>'+
    '<div class="cp"><span>Product:</span> '+prod.name+'</div>'+
    '<div class="cp"><span>Formula:</span> '+(fmap[S.formula]||S.formula)+'</div>'+
    '<div class="cp"><span>Tone:</span> '+S.tone+'</div>'+
    '<div class="cp"><span>Length:</span> '+(lmap[S.length]||S.length)+'</div>';
  ['ctx-pills','ctx-pills-3'].forEach(function(id){var e=document.getElementById(id);if(e)e.innerHTML=html;});
}
async function callAPI(prompt){
  var isNetlify=window.location.hostname.indexOf('netlify.app')>=0||window.location.hostname.indexOf('netlify.com')>=0;
  var endpoint=isNetlify?'/.netlify/functions/claude':'https://api.anthropic.com/v1/messages';
  var bodyObj=isNetlify?{prompt:prompt,maxTokens:3000}:{model:'claude-sonnet-4-6',max_tokens:3000,messages:[{role:'user',content:prompt}]};
  var r=await fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(bodyObj)});
  if(!r.ok){var err=await r.text();throw new Error('API Error '+r.status+': '+err);}
  var d=await r.json();
  if(d.content&&d.content[0]&&d.content[0].text)return d.content[0].text;
  if(d.text)return d.text;
  throw new Error(d.error?d.error.message:'No response from API');
}
function viralRank(v){
  var vl=(v||'').toLowerCase();
  if(vl.indexOf('high')>=0)return 3;
  if(vl.indexOf('medium')>=0)return 2;
  return 1;
}
function parseIdeas(text){
  var out=[];
  var lines=text.split('\n');
  for(var i=0;i<lines.length;i++){
    var line=lines[i];
    var m=line.match(/^\s*\d+[\.)]\s+(.+)/);
    if(m){
      var parts=m[1].split('|');
      if(parts.length>=1){
        out.push({
          title:(parts[0]||'').trim().replace(/\*\*/g,''),
          hook:(parts[1]||'').trim(),
          thumb:(parts[2]||'').trim(),
          viral:(parts[3]||'').trim().replace(/\*\*/g,'')
        });
      }
    }
  }
  out.sort(function(a,b){return viralRank(b.viral)-viralRank(a.viral);});
  return out.slice(0,10);
}
function renderIdeas(list){
  var el=document.getElementById('idea-list');
  el.innerHTML='';
  var lastLevel='';
  var levelColors={high:'#4ade80',medium:'var(--gold)',low:'var(--g4)'};
  var levelLabels={high:'HIGHEST VIRAL',medium:'MEDIUM VIRAL',low:'LOWER VIRAL'};
  for(var i=0;i<list.length;i++){
    var idea=list[i];
    var vl=(idea.viral||'').toLowerCase().indexOf('high')>=0?'high':(idea.viral||'').toLowerCase().indexOf('medium')>=0?'medium':'low';
    if(vl!==lastLevel){
      var div=document.createElement('div');
      div.style.cssText='display:flex;align-items:center;gap:8px;margin:'+(i===0?'0':'10px')+' 0 6px;';
      div.innerHTML='<div style="height:1px;flex:1;background:'+levelColors[vl]+';opacity:.3;"></div>'+
        '<span style="font-size:10px;font-weight:700;color:'+levelColors[vl]+';letter-spacing:.8px;white-space:nowrap;">'+levelLabels[vl]+'</span>'+
        '<div style="height:1px;flex:1;background:'+levelColors[vl]+';opacity:.3;"></div>';
      el.appendChild(div);
      lastLevel=vl;
    }
    var isTop=i===0;
    var rankBadge=isTop?'<div style="background:var(--gold);color:var(--navyd);font-size:9px;font-weight:700;padding:2px 7px;border-radius:4px;margin-bottom:4px;display:inline-block;">TOP PICK - AUTO-SELECTED</div><br>':
      '<div style="background:rgba(255,255,255,.07);color:var(--g4);font-size:9px;font-weight:600;padding:2px 7px;border-radius:4px;margin-bottom:4px;display:inline-block;">#'+(i+1)+'</div><br>';
    var item=document.createElement('div');
    item.className='idea-item'+(isTop?' sel':'');
    item.setAttribute('data-idx',i);
    item.onclick=(function(idx){return function(){selectIdea(idx);};})(i);
    item.innerHTML='<div class="ichk" id="ichk-'+i+'">'+(isTop?'v':'')+'</div>'+
      '<div style="flex:1;">'+rankBadge+
      '<div class="itxt" style="'+(isTop?'color:var(--white);font-weight:600;':'')+'">'+idea.title+'</div>'+
      '<div class="imeta" style="margin-top:4px;">'+idea.hook.substring(0,90)+(idea.hook.length>90?'...':'')+'</div>'+
      '<div class="imeta" style="margin-top:2px;">"'+idea.thumb+'" Viral: <span class="v'+vl+'">'+idea.viral+'</span></div>'+
      '</div>';
    el.appendChild(item);
  }
  if(list.length>0){selIdx=0;document.getElementById('custom-title').value=list[0].title;autoFillKeyPoints(list[0]);}
}
function selectIdea(i){
  selIdx=i;
  var items=document.querySelectorAll('.idea-item');
  for(var j=0;j<items.length;j++){
    items[j].classList.toggle('sel',j===i);
    var chk=document.getElementById('ichk-'+j);
    if(chk)chk.textContent=j===i?'v':'';
  }
  if(ideas[i]){document.getElementById('custom-title').value=ideas[i].title;autoFillKeyPoints(ideas[i]);}
}
function autoFillKeyPoints(idea){
  var kpEl=document.getElementById('key-points');
  if(!kpEl||!idea)return;
  var prod=P[S.pk];
  var title=(idea.title||'').toLowerCase();
  var points=[];
  if(title.indexOf('profit leak')>=0||title.indexOf('draining')>=0||title.indexOf('losing')>=0){
    points=['- Profit Leak 1: Undercharging in naira while tool costs rise in dollars','- Profit Leak 2: Scope creep with no change-order system','- Profit Leak 3: No retainer model - resetting revenue to zero every month','- Profit Leak 4: Non-billable staff time eating into margins','- The fix: Agency Performance Stack system for each leak','- CTA: Free Agency Performance Scorecard at agencyscorecard1.netlify.app'];
  }else if(title.indexOf('client')>=0||title.indexOf('retain')>=0||title.indexOf('ghost')>=0){
    points=['- Why clients leave: getting results but not communicating them','- The silent killer: no formal onboarding or expectation-setting','- How top Nigerian agencies create 12-month retainer relationships','- The client retention playbook: monthly reporting and quarterly reviews','- Why client referrals dry up when you have no retention system','- CTA: Free Agency Performance Scorecard'];
  }else if(title.indexOf('price')>=0||title.indexOf('charg')>=0||title.indexOf('undercharg')>=0){
    points=['- Why Nigerian agencies quote in naira but pay for tools in dollars','- The pricing psychology that makes clients say yes without negotiating','- Value-based pricing vs hourly: what top African agencies charge','- How to present price increases without losing existing clients','- The exact pricing ladder from N150K to N1M+ retainers','- CTA: Agency Performance Stack Workbook on Gumroad'];
  }else if(title.indexOf('scale')>=0||title.indexOf('grow')>=0){
    points=['- The 3 systems every Nigerian agency needs before scaling','- Why hiring more staff before systemising destroys profit margins','- The flywheel model: how one client becomes five without paid ads','- Delegation framework: what to outsource first in Lagos/Abuja','- How to replace yourself as the bottleneck in your agency','- CTA: Agency Performance Stack PRO at agencypss1.netlify.app'];
  }else if(title.indexOf('stuck')>=0||title.indexOf('freelancer')>=0){
    points=['- The mindset shift from freelancer to agency owner in Nigeria','- Why staying at N500K is a systems problem not a skills problem','- The three offers every Nigerian agency needs: entry, core, premium','- How to break the feast-and-famine income cycle permanently','- Building recurring revenue so you start every month above zero','- CTA: Free Agency Performance Scorecard'];
  }else{
    points=['- Core problem: '+prod.pain,'- Why the conventional approach fails Nigerian agency owners','- The 3-step system that solves this specific problem','- Real Nigerian example with naira amounts and results','- How to implement this week not next quarter','- CTA: '+prod.cta];
  }
  kpEl.value=points.join('\n');
  kpEl.style.borderColor='var(--gold)';
  kpEl.style.background='rgba(232,200,0,.08)';
  setTimeout(function(){kpEl.style.borderColor='';kpEl.style.background='';},1500);
}
async function generateIdeas(){
  S.pk=document.getElementById('s-product').value;
  S.formula=document.getElementById('s-formula').value;
  S.tone=document.getElementById('s-tone').value;
  S.length=document.getElementById('s-length').value;
  S.style=document.getElementById('s-style').value;
  var prod=P[S.pk];
  setBL('gen-ideas-btn',true);
  try{
    var styleText='educational how-to';
    if(S.style==='listicle')styleText='listicle/numbered list';
    else if(S.style==='story')styleText='story/case study';
    else if(S.style==='mistake')styleText='common mistakes to avoid';
    else if(S.style==='controversial')styleText='controversial hot take';
    else if(S.style==='flywheel')styleText='Flywheel Masterclass comprehensive deep-dive';
    else if(S.style==='shorts')styleText='YouTube Short 60 seconds punchy';
    var prompt='You are a top YouTube strategist who has grown 50+ channels to 100K+ subscribers. Generate exactly 10 high-converting YouTube video ideas for Wealthora Digital by Alexander E. Reid.\n\n'+
      'Product: '+prod.name+'\n'+
      'Audience: '+prod.audience+'\n'+
      'Pain point: '+prod.pain+'\n'+
      'Style: '+styleText+'\n'+
      'Market: Nigerian and African digital entrepreneurs 2026\n\n'+
      'For EACH idea provide ALL of the following on ONE LINE separated by | :\n'+
      'TITLE (max 60 chars, scroll-stopping, use numbers/power words/naira amounts) | HOOK (exact first sentence spoken) | THUMBNAIL TEXT (3-5 words, punchy) | VIRAL POTENTIAL (Low/Medium/High)\n\n'+
      'Viral scoring: HIGH = universal Nigerian agency pain + specific naira amount or percentage. MEDIUM = relevant but less urgent. LOW = informational only.\n'+
      'Rules: Nigerian/African context in every title. Every title stops mid-scroll. Real pain points, naira amounts, specific outcomes. Number them 1-10. Aim for at least 7 High viral potential ideas.';
    var r=await callAPI(prompt);
    ideas=parseIdeas(r);
    renderIdeas(ideas);
    document.getElementById('idea-card').style.display='block';
    toast('10 ideas generated - Top pick auto-selected');
  }catch(e){toast('Error: '+e.message);}
  setBL('gen-ideas-btn',false,'Generate 10 Video Ideas');
}
async function proceedToPhase2(){
  var title=document.getElementById('custom-title').value.trim();
  var kp=document.getElementById('key-points').value.trim();
  if(!title){toast('Select an idea or type a title first');return;}
  S.pk=document.getElementById('s-product').value;
  S.formula=document.getElementById('s-formula').value;
  S.tone=document.getElementById('s-tone').value;
  S.length=document.getElementById('s-length').value;
  S.style=document.getElementById('s-style').value;
  S.title=title;S.kp=kp;
  addToTracker(title,P[S.pk].name,'Scripting');
  updateCtx();
  goTo(1);
  var pb=document.getElementById('proceed-btn');
  if(pb){pb.disabled=true;pb.innerHTML='<span class="spin"></span> Generating Script, SEO, Thumbnail and Description...';}
  setOB('script-out','Generating Hook and Intro (1/3)...');
  setOB('seo-out','Waiting...');
  setOB('thumb-out','Waiting...');
  setOB('desc-out','Waiting...');
  var prod=P[S.pk];
  var bp=BLUEPRINTS[S.formula]||BLUEPRINTS['ppb'];
  var tone=TONES[S.tone];
  var len=LENGTHS[S.length];
  var kpts=S.kp||'Address the core pain points, provide 3-5 proven solutions with Nigerian examples, bridge to product naturally';
  var ttl=S.title;
  var sec1='',sec2='',sec3='',scriptR='';
  try{
    sec1=await callAPI(
      'You are a world-class YouTube scriptwriter for faceless voiceover channels. Write ONLY the HOOK and INTRO. Stop after INTRO - do not write main content.\n'+
      'TITLE: "'+ttl+'"\n'+
      'PRODUCT: '+prod.name+' | AUDIENCE: '+prod.audience+' | PAIN: '+prod.pain+'\n'+
      'TONE: '+tone+'\n'+
      'FORMULA GUIDE: '+bp+'\n\n'+
      '[HOOK 0:00-0:30]\n'+
      'Bold opening. No greetings. No "In this video". Drop straight into Nigerian pain. 3-4 short sentences. Create a knowledge gap they must close.\n\n'+
      '[INTRO 0:30-1:00]\n'+
      'Tell them WHO this is for, WHAT they will learn, WHY they must watch to the end. Promise a specific outcome. 2-3 sentences.\n\n'+
      'Rules: Write EVERY word spoken. Max 12 words per sentence. Naira amounts. No filler. STOP after INTRO.'
    );
    setOB('script-out',sec1+'\n\nWriting Main Content (2/3)...');
    await new Promise(function(r){setTimeout(r,1200);});
    sec2=await callAPI(
      'You are a world-class YouTube scriptwriter. Write ONLY the MAIN CONTENT section. Do not repeat the hook or intro. Stop before the CTA.\n'+
      'TITLE: "'+ttl+'"\n'+
      'PRODUCT: '+prod.name+' | AUDIENCE: '+prod.audience+' | PAIN: '+prod.pain+'\n'+
      'TONE: '+tone+' | LENGTH TARGET: '+len+'\n'+
      'KEY POINTS TO COVER:\n'+kpts+'\n\n'+
      '[MAIN CONTENT - 1:00 onwards]\n'+
      'Deliver 4-5 points with clear subheadings. Under each point:\n'+
      '- Write EVERY word of the voiceover narration\n'+
      '- Include a real Nigerian example with naira amounts\n'+
      '- Add B-ROLL note with specific footage description after each point\n'+
      '- End each point with a micro-payoff sentence\n\n'+
      '[PATTERN INTERRUPT - midpoint]\n'+
      'After point 2 or 3: insert a shocking Nigerian statistic or bold direct question to reset viewer attention.\n\n'+
      'Rules: Write EVERY word spoken. Max 12 words per sentence. No filler. Lagos/Abuja context. STOP after all content points - do not write CTA.'
    );
    setOB('script-out',sec1+'\n\n'+sec2+'\n\nWriting CTA and Outro (3/3)...');
    await new Promise(function(r){setTimeout(r,1200);});
    sec3=await callAPI(
      'You are a world-class YouTube scriptwriter. Write ONLY the TRANSITION TO CTA, the CTA itself, and the OUTRO. Do not repeat any earlier content.\n'+
      'TITLE: "'+ttl+'"\n'+
      'PRODUCT: '+prod.name+' | CTA GOAL: '+prod.cta+'\n'+
      'TONE: '+tone+'\n\n'+
      '[TRANSITION TO CTA]\n'+
      '2-3 sentences naturally bridging from the content to the offer. Make it feel earned not salesy.\n\n'+
      '[CTA - placed at 70% mark]\n'+
      'Deliver this specific CTA: '+prod.cta+'\n'+
      'Make it urgent, specific, and benefit-focused. Tell them exactly what to do next. 60-75 words spoken.\n\n'+
      '[OUTRO]\n'+
      'Thank them briefly. Tease the NEXT video with a specific topic. Ask them to subscribe with ONE specific reason tied to what they just learned. End with "See you next time."\n\n'+
      'Rules: Write EVERY word spoken. Conversational. No hard sell. Nigerian context.'
    );
    scriptR=sec1+'\n\n'+sec2+'\n\n'+sec3;
    setOB('script-out',scriptR);
    var words=scriptR.trim().split(/\s+/).filter(function(x){return x.length>0;}).length;
    var mins=Math.round(words/130);
    var wcEl=document.getElementById('wc-display');
    if(wcEl)wcEl.textContent='~'+words+' words ~'+mins+' min read aloud';
    setOB('seo-out','Generating SEO package...');
  }catch(e){
    setOB('script-out','Script failed: '+e.message+'. Wait 60 seconds and try again.');
    if(pb){pb.disabled=false;pb.innerHTML='Generate Script, SEO, Thumbnail and Description';}
    return;
  }
  var seoR='';
  try{
    seoR=await callAPI(
      'Complete YouTube SEO package for a Nigerian faceless channel.\n'+
      'TITLE: "'+ttl+'" | PRODUCT: '+prod.name+' | MARKET: Nigerian audience (Lagos, Abuja) | TOPICS: '+prod.topics.join(', ')+'\n'+
      'Provide:\n'+
      '1. OPTIMIZED TITLES (3 variations - A: curiosity, B: number-based, C: outcome-based. Star the strongest)\n'+
      '2. PRIMARY KEYWORD + estimated monthly searches\n'+
      '3. SECONDARY KEYWORDS (8 related terms)\n'+
      '4. TAGS (30 comma-separated - mix exact, broad, Nigerian-specific, long-tail)\n'+
      '5. CHAPTERS (8 timestamps for 10-min video - format: 0:00 Intro)\n'+
      '6. HASHTAGS (25 - 5 specific, 10 niche, 10 broad Nigerian/African)\n'+
      '7. FIRST 48 HOURS CHECKLIST (exact actions after publishing)'
    );
    setOB('seo-out',seoR);
    setOB('thumb-out','Generating thumbnail brief...');
  }catch(e){setOB('seo-out','SEO failed: '+e.message);}
  await new Promise(function(r){setTimeout(r,800);});
  var thumbR='';
  try{
    thumbR=await callAPI(
      'Detailed Canva thumbnail design brief for YouTube (1280x720px).\n'+
      'TITLE: "'+ttl+'" | PRODUCT: '+prod.name+' | STYLE: Bold Text + Reaction\n'+
      'BRAND: Navy (#1A1FA8) + Gold (#E8C800) - Wealthora Digital\n'+
      'Provide:\n'+
      '1. VISUAL CONCEPT (left/centre/right breakdown)\n'+
      '2. MAIN TEXT OVERLAY (exact words, max 5, punchy)\n'+
      '3. SUB-TEXT (optional, max 4 words)\n'+
      '4. BACKGROUND (exact Canva color or search term)\n'+
      '5. FONTS (name, weight, size, color)\n'+
      '6. VISUAL ELEMENTS (each: what, where, color)\n'+
      '7. CANVA SEARCH TERMS (exact words to type)\n'+
      '8. CTR PSYCHOLOGY (why this makes someone click - 2 sentences)\n'+
      '9. 3 MISTAKES TO AVOID'
    );
    setOB('thumb-out',thumbR);
    setOB('desc-out','Generating description...');
  }catch(e){setOB('thumb-out','Thumbnail failed: '+e.message);}
  await new Promise(function(r){setTimeout(r,800);});
  var descR='';
  try{
    descR=await callAPI(
      'Complete SEO-optimised YouTube description - copy-paste ready.\n'+
      'TITLE: "'+ttl+'" | PRODUCT: '+prod.name+' | TOPICS: '+prod.topics.join(', ')+'\n'+
      'FORMAT:\n'+
      'HOOK PARAGRAPH (lines 1-3 before Show More - keyword in first 100 chars)\n'+
      'WHAT YOU WILL LEARN\n'+
      '- [4-6 specific bullet points - action verbs]\n'+
      'TIMESTAMPS\n'+
      '00:00 - Introduction\n'+
      '[create 7 logical chapters]\n'+
      'LINKS (THIS ORDER):\n'+
      'LINK 1 - Full Masterclass: [paste your Flywheel URL here]\n'+
      'LINK 2 - Free Agency Scorecard: https://agencyscorecard1.netlify.app\n'+
      'LINK 3 - Agency Stack Workbook ($47): https://wealthoradigital.gumroad.com\n'+
      'LINK 4 - Agency Stack PRO ($197): https://agencypss1.netlify.app\n'+
      'LINK 5 - Digital Fatigue Reset: https://selar.co\n'+
      'Instagram: @WealthoraDigital\n'+
      'AFFILIATE TOOLS:\n'+
      'ElevenLabs: [your affiliate link]\n'+
      'Canva Pro: [your affiliate link]\n'+
      'CapCut: [your affiliate link]\n'+
      'ABOUT THIS CHANNEL\n'+
      'Alexander E. Reid is an agency growth strategist helping Nigerian and African digital entrepreneurs scale their income through proven systems, AI tools and digital products. New videos every Wednesday and Saturday.\n'+
      '[25 hashtags - 5 specific, 10 niche, 10 broad Nigerian/African]\n'+
      'Keep total under 4800 characters.'
    );
    setOB('desc-out',descR);
  }catch(e){setOB('desc-out','Description failed: '+e.message);}
  updateTrackerStatus(S.title,'Scripting');
  document.getElementById('fwd-banner').classList.add('show');
  if(pb){pb.disabled=false;pb.innerHTML='Generate Script, SEO, Thumbnail and Description';}
  toast('All outputs ready - review each tab above');
}
async function regenScript(){
  if(!S.title){toast('Go back to Phase 1 and select a topic first');return;}
  setBL('regen-script-btn',true);
  var prod=P[S.pk];
  var bp=BLUEPRINTS[S.formula]||BLUEPRINTS['ppb'];
  var tone=TONES[S.tone];
  var kpts=S.kp||'core pain points and 3-5 solutions with Nigerian examples';
  try{
    setOB('script-out','Rewriting Hook and Intro (1/3)...');
    var rs1=await callAPI('Rewrite ONLY the HOOK and INTRO of this YouTube script. Stronger, punchier, more Nigerian.\nTITLE: "'+S.title+'" | PRODUCT: '+prod.name+' | AUDIENCE: '+prod.audience+' | TONE: '+tone+'\n[HOOK 0:00-0:30] Bold. No greetings. Nigerian pain. Creates curiosity. 3-4 sentences.\n[INTRO 0:30-1:00] Who it is for, what they learn, why watch to end. 2-3 sentences.\nWrite EVERY word spoken. Max 12 words per sentence. Stop after INTRO.');
    setOB('script-out',rs1+'\n\nRewriting Main Content (2/3)...');
    await new Promise(function(r){setTimeout(r,1200);});
    var rs2=await callAPI('Rewrite ONLY the MAIN CONTENT of this YouTube script with stronger Nigerian examples and naira amounts.\nTITLE: "'+S.title+'" | PRODUCT: '+prod.name+' | KEY POINTS: '+kpts+' | TONE: '+tone+'\nFORMULA GUIDE: '+bp+'\n[MAIN CONTENT] 4-5 subheaded points. Each: full narration every word + Nigerian naira example + B-ROLL note + micro-payoff.\n[PATTERN INTERRUPT] Bold question or stat after point 2-3.\nWrite EVERY word. Max 12 words per sentence. Stop after all points.');
    setOB('script-out',rs1+'\n\n'+rs2+'\n\nRewriting CTA and Outro (3/3)...');
    await new Promise(function(r){setTimeout(r,1200);});
    var rs3=await callAPI('Rewrite ONLY the CTA and OUTRO of this YouTube script. More urgent, more specific.\nTITLE: "'+S.title+'" | CTA GOAL: '+prod.cta+' | TONE: '+tone+'\n[TRANSITION TO CTA] 2-3 bridge sentences. Natural not forced.\n[CTA at 70% mark] '+prod.cta+'. Urgent, specific, benefit-focused. 60-75 words.\n[OUTRO] Tease next specific video. Subscribe ask. End: "See you next time."\nWrite EVERY word spoken.');
    var full=rs1+'\n\n'+rs2+'\n\n'+rs3;
    setOB('script-out',full);
    var w=full.trim().split(/\s+/).filter(function(x){return x.length>0;}).length;
    var wcR=document.getElementById('wc-display');
    if(wcR)wcR.textContent='~'+w+' words ~'+Math.round(w/130)+' min read aloud';
    toast('Script regenerated - '+w+' words');
  }catch(e){toast('Error: '+e.message);}
  setBL('regen-script-btn',false,'Regenerate Script');
}
async function regenHook(){
  if(!S.title){toast('Go back to Phase 1 and select a topic first');return;}
  setBL('regen-hook-btn',true);
  document.getElementById('hook-card').style.display='block';
  setOB('hook-out','Generating 5 hook variations...');
  var prod=P[S.pk];
  try{
    var r=await callAPI('Write 5 completely different YouTube video hook scripts (first 30 seconds each) for a faceless voiceover channel.\nTITLE: "'+S.title+'" | PRODUCT: '+prod.name+' | AUDIENCE: '+prod.audience+'\nHook 1 - SHOCKING STATISTIC: Open with a specific alarming Nigerian number or data point.\nHook 2 - STORY OPENING: Start mid-scene in a relatable Lagos/Abuja business situation. No setup.\nHook 3 - DIRECT ACCUSATION: Call out exactly what the viewer is doing wrong. Bold and direct.\nHook 4 - BOLD CONTROVERSIAL CLAIM: State something that goes against conventional wisdom in Nigerian digital space.\nHook 5 - VIVID SCENARIO: Paint a specific scene the viewer recognises immediately.\nRULES: First word never If, Have you, Hey, or Welcome. Write EVERY word spoken. Nigerian context. Each ends with reason to keep watching. Label Hook 1-5.');
    setOB('hook-out',r);
    toast('5 hooks generated - pick the strongest');
  }catch(e){setOB('hook-out','Error: '+e.message);}
  setBL('regen-hook-btn',false,'New Hooks');
}
async function regenCTA(){
  if(!S.title){toast('Go back to Phase 1 and select a topic first');return;}
  setBL('regen-cta-btn',true);
  document.getElementById('cta-card').style.display='block';
  setOB('cta-out','Generating 3 CTA variations...');
  var prod=P[S.pk];
  try{
    var r=await callAPI('Write 3 YouTube CTA scripts (60-90 seconds each). Write EVERY word that will be spoken.\nPRODUCT: '+prod.name+' | AUDIENCE: '+prod.audience+' | LINK: '+prod.link+' | GOAL: '+prod.cta+'\nCTA 1 - URGENCY (FOMO): Creates fear of missing out. Specific about what they get. Clear next step.\nCTA 2 - VALUE STACK: List exactly what they get. Stack the value. Make the free offer feel like a steal.\nCTA 3 - PAIN AMPLIFICATION: Remind them of the exact pain from the video. Agitate briefly. Position product as relief.\nRULES: Nigerian context. Conversational not salesy. Placed at 70% mark. Label CTA Option 1/2/3.');
    setOB('cta-out',r);
    toast('3 CTAs generated - pick one for 70% mark');
  }catch(e){setOB('cta-out','Error: '+e.message);}
  setBL('regen-cta-btn',false,'New CTAs');
}
async function analyzeAnalytics(){
  var prob=document.getElementById('analytics-in').value.trim();
  if(!prob){toast('Describe your analytics problem first');return;}
  setBL('analytics-btn',true);
  try{
    var r=await callAPI('YouTube analytics consultant diagnosing Wealthora Digital - Nigerian faceless channel (agency growth, digital products, African entrepreneurs).\nPROBLEM: "'+prob+'"\n\nDIAGNOSIS REPORT:\n1. ROOT CAUSE - the actual specific reason (not vague)\n2. IMMEDIATE FIXES - 3 specific actions this week with exact steps\n3. SCRIPT FIX - specific change to make in next video script\n4. THUMBNAIL/TITLE FIX - exact change to test\n5. SEO FIX - tag, description or keyword changes\n6. BENCHMARKS - good/average/poor for Nigerian business faceless channel (0-1K, 1K-10K, 10K+)\n7. 30-DAY RECOVERY PLAN - Week 1, 2, 3, 4 specific tasks\n8. LEADING INDICATOR - the one metric that if it improves fixes the reported problem');
    setOB('analytics-out',r);
    toast('AI diagnosis ready');
  }catch(e){setOB('analytics-out','Error: '+e.message);}
  setBL('analytics-btn',false,'Get AI Diagnosis');
}
function downloadScript(){
  var el=document.getElementById('script-out');
  if(!el||el.classList.contains('empty')){toast('No script to download yet');return;}
  var text=el.textContent;
  if(!text||text.length<50){toast('Generate a script first');return;}
  var blob=new Blob([text],{type:'text/plain;charset=utf-8'});
  var url=URL.createObjectURL(blob);
  var a=document.createElement('a');
  var title=(S.title||'script').replace(/[^a-z0-9]/gi,'_').toLowerCase().substring(0,40);
  a.href=url;a.download='WD_Script_'+title+'.txt';
  document.body.appendChild(a);a.click();
  document.body.removeChild(a);URL.revokeObjectURL(url);
  toast('Script downloaded as .txt file');
}
function markPublished(){
  updateTrackerStatus(S.title,'Published');
  toast('Video marked as Published!');
  goTo(2);
  setTimeout(function(){var t=document.querySelector('#p2 .stab:nth-child(3)');if(t)t.click();},100);
}
function addToTracker(title,product,status){
  if(!title)return;
  var exists=false;
  for(var i=0;i<videos.length;i++){if(videos[i].title.toLowerCase()===title.toLowerCase()){exists=true;break;}}
  if(!exists){
    videos.push({id:Date.now(),title:title.substring(0,80),product:product,status:status,date:new Date().toISOString().split('T')[0]});
    try{localStorage.setItem('wyd_v4',JSON.stringify(videos));}catch(e){}
  }
  renderTracker();
}
function updateTrackerStatus(title,status){
  if(!title)return;
  for(var i=0;i<videos.length;i++){if(videos[i].title.toLowerCase()===title.toLowerCase()){videos[i].status=status;break;}}
  try{localStorage.setItem('wyd_v4',JSON.stringify(videos));}catch(e){}
  renderTracker();
}
function removeVid(id){
  videos=videos.filter(function(v){return v.id!==id;});
  try{localStorage.setItem('wyd_v4',JSON.stringify(videos));}catch(e){}
  renderTracker();
}
function updateVidStatus(id,status){
  for(var i=0;i<videos.length;i++){if(videos[i].id===id){videos[i].status=status;break;}}
  try{localStorage.setItem('wyd_v4',JSON.stringify(videos));}catch(e){}
  renderTracker();
}
function renderTracker(){
  var tbody=document.getElementById('tbody');
  var countEl=document.getElementById('vid-count');
  if(countEl)countEl.textContent=videos.length+' video'+(videos.length!==1?'s':'');
  if(!tbody)return;
  if(videos.length===0){
    tbody.innerHTML='<tr><td colspan="5" style="color:var(--g6);text-align:center;padding:16px;">No videos yet. Complete Phase 1 to start tracking.</td></tr>';
    var mbEl=document.getElementById('m-bar');var mcEl=document.getElementById('m-count');
    if(mbEl)mbEl.style.width='0%';if(mcEl)mcEl.textContent='0 / 8 target';
    return;
  }
  var statuses=['Idea','Scripting','Voiceover','Editing','Ready','Published'];
  var rows='';
  for(var i=0;i<videos.length;i++){
    var v=videos[i];
    var opts='';
    for(var j=0;j<statuses.length;j++){
      opts+='<option value="'+statuses[j]+'"'+(statuses[j]===v.status?' selected':'')+'>'+statuses[j]+'</option>';
    }
    rows+='<tr>'+
      '<td style="max-width:150px;word-break:break-word;font-size:12px;">'+v.title+'</td>'+
      '<td style="font-size:11px;color:var(--g4);">'+v.product+'</td>'+
      '<td><select onchange="updateVidStatus('+v.id+',this.value)" style="background:rgba(255,255,255,.07);border:1px solid rgba(232,200,0,.2);border-radius:6px;padding:3px 6px;color:var(--white);font-size:11px;margin:0;width:auto;">'+opts+'</select></td>'+
      '<td style="font-size:11px;color:var(--g4);">'+(v.date||'-')+'</td>'+
      '<td><button onclick="removeVid('+v.id+')" style="background:none;border:none;color:var(--g6);cursor:pointer;font-size:16px;">x</button></td>'+
    '</tr>';
  }
  tbody.innerHTML=rows;
  var pub=videos.filter(function(v){return v.status==='Published';}).length;
  var mbEl2=document.getElementById('m-bar');var mcEl2=document.getElementById('m-count');
  if(mbEl2)mbEl2.style.width=Math.min((pub/8)*100,100)+'%';
  if(mcEl2)mcEl2.textContent=pub+' / 8 target';
}
function newVideo(){
  S={pk:'agency',title:'',formula:'ppb',tone:'authoritative',length:'medium',style:'educational',kp:''};
  var ic=document.getElementById('idea-card');if(ic)ic.style.display='none';
  var ct=document.getElementById('custom-title');if(ct)ct.value='';
  var kp=document.getElementById('key-points');if(kp)kp.value='';
  var il=document.getElementById('idea-list');if(il)il.innerHTML='';
  var fb=document.getElementById('fwd-banner');if(fb)fb.classList.remove('show');
  var hc=document.getElementById('hook-card');if(hc)hc.style.display='none';
  var cc=document.getElementById('cta-card');if(cc)cc.style.display='none';
  var wcEl=document.getElementById('wc-display');if(wcEl)wcEl.textContent='';
  var fh=document.getElementById('formula-hint');if(fh){fh.textContent='';fh.style.display='none';}
  var sh=document.getElementById('style-hint');if(sh){sh.textContent='';sh.style.display='none';}
  ['script-out','seo-out','thumb-out','desc-out','hook-out','cta-out','analytics-out'].forEach(function(id){setOB(id,'');});
  selIdx=-1;ideas=[];
  goTo(0);
  toast('Ready for your next video!');
}
document.addEventListener('DOMContentLoaded',function(){
  onFormulaChange();
  renderTracker();
});
</script>
</body>
</html>
