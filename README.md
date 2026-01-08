## Video Showcase
https://www.youtube.com/watch?v=dPqnsJ8zkEQ&ab_channel=RencellTobelonia

## Requirements for setup


### Go to backend
```sh
cd backend/
```

### Create virtual environment
```sh
python -m venv venv
```

### activate virtual environment (recommend to use command prompt and not powershell)
```sh
venv\Scripts\activate
```

### pip installs
```sh
pip install -r requirements.txt
```
### Go to backend
```sh
cd sms_backend/
```

### Database migrations
```sh
manage.py migrate
```

### Django run server
```sh
manage.py runserver
```


# frontend-sms

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
cd frontend-sms/
```

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

# Alternatively for easy build use start.sh (Required Bash)

## Open bash terminal and type

```sh
chmod +x ./setup.sh
```
## Then run the command

```sh
./setup.sh
```
## Done
