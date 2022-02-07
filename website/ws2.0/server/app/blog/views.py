from flask import render_template, make_response

from . import blog

@blog.route('/posts', methods=['GET'])
def blog_home():
  template = render_template('blog/blog_home.html')
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@blog.route('/posts/<int:post_id>', methods=['GET'])
def blog_post(post_id):
  #id = request.args.get(post_id, type=int)
  filename = 'post'+str(post_id)+'.html'
  template = render_template('blog/'+filename, post_id=post_id)
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response
