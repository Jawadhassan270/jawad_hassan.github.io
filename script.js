const btn=document.querySelector('.menu-btn'),links=document.querySelector('.nav-links');if(btn&&links){btn.addEventListener('click',()=>{links.classList.toggle('open');btn.setAttribute('aria-expanded',links.classList.contains('open'))});document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));}
// Project image lightbox
const lightbox=document.getElementById('imageLightbox');
const lightboxImage=lightbox?.querySelector('.lightbox-image');
const closeLightbox=()=>{if(!lightbox)return;lightbox.classList.remove('open');lightbox.setAttribute('aria-hidden','true');document.body.style.overflow='';};
const openLightbox=(img)=>{if(!lightbox||!lightboxImage)return;lightboxImage.src=img.src;lightboxImage.alt=img.alt||'Project image';lightbox.classList.add('open');lightbox.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';};
document.querySelectorAll('.project-image').forEach(img=>{img.addEventListener('click',()=>openLightbox(img));img.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openLightbox(img);}});});
lightbox?.querySelector('.lightbox-close')?.addEventListener('click',closeLightbox);
lightbox?.addEventListener('click',e=>{if(e.target===lightbox)closeLightbox();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeLightbox();});
