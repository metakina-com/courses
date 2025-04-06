
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

/**
 * 处理请求并返回响应
 * @param {Request} request
 */
async function handleRequest(request) {
  const url = new URL(request.url)
  
  // 跟踪用户访问数据
  const cfAnalytics = {
    pathname: url.pathname,
    country: request.headers.get('cf-ipcountry'),
    userAgent: request.headers.get('user-agent'),
    timestamp: new Date().toISOString()
  }
  
  // 记录访问数据到Cloudflare KV (示例)
  // await ANALYTICS_NAMESPACE.put(`visit_${Date.now()}`, JSON.stringify(cfAnalytics))
  
  // 从Cloudflare Pages获取原始响应
  let response = await fetch(request)
  
  // 添加安全和缓存相关的头信息
  response = new Response(response.body, response)
  response.headers.set('X-XSS-Protection', '1; mode=block')
  response.headers.set('X-Content-Type-Options', 'nosniff')
  response.headers.set('X-Frame-Options', 'DENY')
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin')
  response.headers.set('Feature-Policy', "camera 'none'; microphone 'none'")
  
  return response
}
