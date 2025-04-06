
/**
 * Cloudflare Worker script for edge functionality
 */

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // URL parsing
  const url = new URL(request.url)
  const path = url.pathname

  // Clone the request to ensure we can read the body later if needed
  const requestClone = request.clone()

  // Add security headers
  let response = await fetch(request)
  response = new Response(response.body, response)
  
  response.headers.set('X-XSS-Protection', '1; mode=block')
  response.headers.set('X-Content-Type-Options', 'nosniff')
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin')
  response.headers.set('Feature-Policy', "camera 'none'; microphone 'none'")
  response.headers.set('Content-Security-Policy', "default-src 'self'; script-src 'self' static.cloudflareinsights.com challenges.cloudflare.com 'unsafe-inline'; style-src 'self' 'unsafe-inline';")

  // Cache control for static assets
  if (path.match(/\.(jpg|jpeg|png|gif|ico|css|js)$/i)) {
    response.headers.set('Cache-Control', 'public, max-age=86400')
  } else {
    response.headers.set('Cache-Control', 'no-cache, no-store, must-revalidate')
  }

  return response
}
