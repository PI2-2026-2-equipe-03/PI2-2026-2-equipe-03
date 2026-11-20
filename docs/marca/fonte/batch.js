// uso: node batch.js jobs.json   jobs: [[in.svg,out.png,width|null,bg|null], ...]
const {Resvg}=require('@resvg/resvg-js');const fs=require('fs');const path=require('path');
for(const [i,o,w,bg] of JSON.parse(fs.readFileSync(process.argv[2]))){
  fs.mkdirSync(path.dirname(o),{recursive:true});
  const r=new Resvg(fs.readFileSync(i),{fitTo:w?{mode:'width',value:w}:{mode:'original'},background:bg||undefined,font:{loadSystemFonts:false}});
  fs.writeFileSync(o,r.render().asPng());
}
