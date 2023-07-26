import os

def deploy():
    os.system('python manage.py collectstatic')
    os.system('git add -A')
    os.system('git commit -m "Deploying to GitHub Pages"')
    os.system('git push origin gh-pages')

if __name__ == '__main__':
    deploy()