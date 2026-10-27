import { ImageResponse } from '@vercel/og';
export const config = { runtime: 'edge' };
const h=(type,style,children)=>({type,props:{style,children}});
export default async function handler(req){
  const url=new URL(req.url);const slug=url.searchParams.get('slug')||'';
  const arts=await fetch(new URL('/build/articles.json',url.origin)).then(r=>r.json());
  const a=arts.find(x=>x.slug===slug)||arts[0];
  const picks=a.sections.reduce((n,s)=>n+(s[1].match(/class="pick"/g)||[]).length,0);
  const img=a.img.startsWith('http')?a.img.replace(/w=\d+/,'w=1000'):url.origin+'/img/'+a.img;
  const title=a.title.replace(/\s*\(20\d\d\)/,'');
  const el=h('div',{width:'1000px',height:'1500px',display:'flex',flexDirection:'column',background:'#070d1a',position:'relative'},[
    {type:'img',props:{src:img,width:1000,height:940,style:{position:'absolute',top:0,left:0,width:'1000px',height:'940px',objectFit:'cover'}}},
    h('div',{position:'absolute',top:0,left:0,width:'1000px',height:'940px',display:'flex',background:'linear-gradient(180deg, rgba(7,13,26,0.05) 45%, #070d1a 100%)'},''),
    h('div',{position:'absolute',top:56,left:56,display:'flex',background:'linear-gradient(90deg,#3b82f6,#22d3ee)',color:'#fff',fontSize:32,fontWeight:700,padding:'14px 28px',borderRadius:999},picks?`${picks} picks compared`:'Step-by-step guide'),
    h('div',{position:'absolute',left:64,right:64,bottom:70,display:'flex',flexDirection:'column'},[
      h('div',{color:'#22d3ee',fontSize:30,fontWeight:700,letterSpacing:4,textTransform:'uppercase',marginBottom:22},`${a.tag} · ${a.updated}`),
      h('div',{color:'#fff',fontSize:90,fontWeight:800,lineHeight:1.05,letterSpacing:-2},title),
      h('div',{color:'#cbd5e1',fontSize:36,lineHeight:1.35,marginTop:26},a.desc.length>115?a.desc.slice(0,112)+'…':a.desc),
      h('div',{display:'flex',alignItems:'center',justifyContent:'space-between',marginTop:46,paddingTop:34,borderTop:'2px solid #1c2a47'},[
        h('div',{display:'flex',alignItems:'center',color:'#fff',fontSize:34,fontWeight:800},[
          h('div',{width:54,height:54,borderRadius:14,background:'linear-gradient(135deg,#3b82f6,#22d3ee)',marginRight:16},''),'The Home ',h('span',{color:'#60a5fa',margin:'0 10px'},'Desk'),'Guide']),
        h('div',{background:'#fff',color:'#070d1a',fontSize:30,fontWeight:800,padding:'18px 30px',borderRadius:16},'Read the guide →')])])]);
  return new ImageResponse(el,{width:1000,height:1500,headers:{'cache-control':'public, max-age=86400'}});
}
