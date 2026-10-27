import { ImageResponse } from '@vercel/og';
export const config = { runtime: 'edge' };
const F='https://cdn.jsdelivr.net/npm/@fontsource/plus-jakarta-sans@5.0.20/files/plus-jakarta-sans-latin-';
const h=(type,style,children)=>({type,props:{style,children}});
export default async function handler(req){
  const url=new URL(req.url);const slug=url.searchParams.get('slug')||'';
  const [arts,f8,f6]=await Promise.all([fetch(new URL('/build/articles.json',url.origin)).then(r=>r.json()),
    fetch(F+'800-normal.woff').then(r=>r.arrayBuffer()),fetch(F+'600-normal.woff').then(r=>r.arrayBuffer())]);
  const a=arts.find(x=>x.slug===slug)||arts[0];
  const html=a.sections.map(s=>s[1]).join('');
  const names=[...html.matchAll(/<div class="pick">[\s\S]*?<h3>([^<]+)<\/h3>/g)].map(m=>m[1].replace(/&quot;/g,'"'));
  const img=a.img.startsWith('http')?a.img.replace(/w=\d+/,'w=1000'):url.origin+'/img/'+a.img;
  let title=a.title.replace(/\s*\(20\d\d\)/,'');let num='';
  const m=title.match(/^(\d+)\s+(.*)$/);if(m){num=m[1];title=m[2]}
  const list=names.slice(0,3).map(n=>h('div',{display:'flex',alignItems:'center',color:'#e2e8f0',fontSize:32,fontWeight:600,marginTop:14},[
    h('div',{width:38,height:38,borderRadius:10,background:'#22d3ee',color:'#04111f',display:'flex',alignItems:'center',justifyContent:'center',marginRight:18},[{type:'img',props:{src:"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%2304111f' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E",width:26,height:26}}]),n]));
  const el=h('div',{width:'1000px',height:'1500px',display:'flex',flexDirection:'column',background:'#050a14',fontFamily:'Jakarta',position:'relative'},[
    {type:'img',props:{src:img,width:1000,height:820,style:{position:'absolute',top:0,left:0,width:'1000px',height:'820px',objectFit:'cover'}}},
    h('div',{position:'absolute',top:0,left:0,width:'1000px',height:'820px',display:'flex',background:'linear-gradient(180deg, rgba(5,10,20,0.85) 0%, rgba(5,10,20,0) 26%, rgba(5,10,20,0) 55%, #050a14 100%)'},''),
    h('div',{position:'absolute',top:54,left:60,right:60,display:'flex',justifyContent:'space-between',alignItems:'center'},[
      h('div',{display:'flex',alignItems:'center',color:'#fff',fontSize:30,fontWeight:800,background:'rgba(5,10,20,0.75)',padding:'10px 20px 10px 10px',borderRadius:999},[h('div',{width:46,height:46,borderRadius:12,background:'linear-gradient(135deg,#3b82f6,#22d3ee)',marginRight:14},''),'The Home Desk Guide']),
      h('div',{display:'flex',background:'rgba(5,10,20,0.75)',border:'2px solid #22d3ee',color:'#fff',fontSize:26,fontWeight:800,padding:'10px 22px',borderRadius:999,letterSpacing:2},(a.updated||'').toUpperCase())]),
    h('div',{position:'absolute',left:60,right:60,top:660,bottom:60,display:'flex',flexDirection:'column'},[
      num?h('div',{display:'flex',alignItems:'flex-end'},[h('div',{fontSize:210,fontWeight:800,lineHeight:0.85,color:'#22d3ee',letterSpacing:-8,marginRight:20},num),
        h('div',{display:'flex',flexDirection:'column',color:'#fff',fontSize:40,fontWeight:800,letterSpacing:6,paddingBottom:10},[h('div',{},'TOP PICKS'),h('div',{color:'#94a3b8',fontSize:26,letterSpacing:4},'COMPARED')])]):h('div',{color:'#22d3ee',fontSize:34,fontWeight:800,letterSpacing:6},'BUYING GUIDE'),
      h('div',{color:'#fff',fontSize:title.length>34?76:88,fontWeight:800,lineHeight:1.02,letterSpacing:-3,marginTop:28},title),
      h('div',{display:'flex',flexDirection:'column',marginTop:30},list),
      h('div',{display:'flex',marginTop:'auto',background:'linear-gradient(90deg,#3b82f6,#22d3ee)',borderRadius:22,padding:'26px 0',justifyContent:'center',color:'#fff',fontSize:36,fontWeight:800},'See the full comparison →')])]);
  return new ImageResponse(el,{width:1000,height:1500,fonts:[{name:'Jakarta',data:f8,weight:800},{name:'Jakarta',data:f6,weight:600}],headers:{'cache-control':'public, max-age=600, s-maxage=600'}});
}
