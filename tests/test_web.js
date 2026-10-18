"use strict";
const assert = require("assert"), fs = require("fs"), path = require("path"), vm = require("vm");
const W = require("../docs/app/warroom.js");
const ctx = {}; vm.runInNewContext(fs.readFileSync(path.join(__dirname, "../docs/app/data.js"), "utf8").replace("var WR_DATA", "this.WR_DATA"), ctx);
const D = ctx.WR_DATA, V = require("./web_vectors.json");
let n = 0;
V.forEach((v) => {
  const c = D.crises.find((x) => x.crisis_id === v.crisis_id);
  const st = W.exercise(c, D.profiles);
  assert.strictEqual(st.length, v.stages.length, v.crisis_id);
  st.forEach((s, i) => {
    const e = v.stages[i], d = s.decision, tag = `${v.crisis_id}#${i}`;
    assert.strictEqual(d.recommended_option, e.recommended_option, tag);
    assert.deepStrictEqual(d.votes, e.votes, tag);
    assert.ok(Math.abs(d.consensus_score - e.consensus_score) < 0.051, tag);
    assert.ok(Math.abs(d.dissent_score - e.dissent_score) < 0.051, tag);
    assert.ok(Math.abs(d.confidence - e.confidence) < 0.0051, tag);
    for (const k in e.option_scores) assert.ok(Math.abs(d.option_scores[k] - e.option_scores[k]) < 2e-4, tag + k);
    assert.strictEqual(d.red_team.length, e.red_team_count, tag);
    assert.strictEqual(d.review_required, e.review_required, tag);
    n++;
  });
});
console.log(`ok: ${n} exercise stages match the Python reference`);
