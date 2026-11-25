const fs=require('fs'),p='wle/package/';
const load=(lv)=>['english','american','british'].flatMap(r=>JSON.parse(fs.readFileSync(`${p}${r}-words-${lv}.json`)));
const ok=w=>/^[a-z]+$/.test(w)&&w.length>=2&&w.length<=12;
const common=new Set([10,20,35].flatMap(load).filter(ok));
const all=new Set([10,20,35,40,50,55,60,70].flatMap(load).filter(ok));
// group by length for compactness: {"3":"cat dog ...", ...}
const grp=s=>{const g={};for(const w of [...s].sort()){(g[w.length]??=[]).push(w)}for(const k in g)g[k]=g[k].join(' ');return g};
const out={common:grp(common),all:grp([...all].filter(w=>!common.has(w)))};
fs.writeFileSync('words.json',JSON.stringify(out));
console.log('common',common.size,'all',all.size,'bytes',fs.statSync('words.json').size);
const cl={};for(const w of common)cl[w.length]=(cl[w.length]||0)+1;console.log(cl);
