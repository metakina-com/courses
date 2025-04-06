
// METAKINA RWA课程平台自定义JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // 页面加载时淡入效果
  document.body.classList.add('fade-in');
  
  // 为课程卡片添加进入视图时的动画效果
  if ('IntersectionObserver' in window) {
    const courseCards = document.querySelectorAll('.course-card');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });
    
    courseCards.forEach(card => {
      observer.observe(card);
    });
  }
  
  // 自动更新学习进度条（示例逻辑）
  const progressBars = document.querySelectorAll('.progress-bar');
  progressBars.forEach(bar => {
    // 这里可以从本地存储或API获取实际进度
    // 这里使用随机值作为示例
    const progress = Math.floor(Math.random() * 100);
    bar.style.width = progress + '%';
    
    // 添加进度文本
    const progressText = bar.parentElement.querySelector('.progress-text');
    if (progressText) {
      progressText.textContent = progress + '%';
    }
  });
  
  // 内容目录固定
  const tableOfContents = document.querySelector('.md-sidebar--secondary');
  if (tableOfContents) {
    let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    window.addEventListener('scroll', function() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      
      if (scrollTop > 100) {
        tableOfContents.classList.add('toc-fixed');
      } else {
        tableOfContents.classList.remove('toc-fixed');
      }
      
      lastScrollTop = scrollTop;
    });
  }
  
  // 平滑滚动到锚点
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: 'smooth'
        });
      }
    });
  });
});

// 主题切换动画
document.querySelector('.md-header__button.md-icon').addEventListener('click', function() {
  document.body.classList.add('theme-transition');
  setTimeout(() => {
    document.body.classList.remove('theme-transition');
  }, 1000);
});
