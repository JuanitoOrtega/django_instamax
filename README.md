# Install tailwindcss
## Node
```bash
mkdir node
cd node
npm init -y
```
## Install tailwindcss
```bash
npm install -D tailwindcss
npx tailwindcss init
```
## Edit tailwind.config.js
```bash
content: [
    '../templates/**/*.html',
    '../**/templates/**/*.html',
    '../**/forms.py',
],
```
## Edit package.json
```bash
"scripts": {
    "tailwind": "tailwind build -i ../static/css/tailwind.css -o ../static/css/styles.css --watch"
},
```
## Run tailwind
```bash
npm run tailwind
```
# Install clean-css-cli
```bash
npm install clean-css-cli
```
## Edit package.json
```bash
"scripts": {
    "tailwind": "tailwind build -i ../static/css/tailwind.css -o ../static/css/styles.css --watch",
    "minify": "cleancss ../static/css/styles.css -o ../static/css/styles.min.css"
},
```
# Run minify
```bash
npm run minify
```
# Install whitenoise
```bash
pip install whitenoise
```
# Run collectstatic
```bash
python manage.py collectstatic
```