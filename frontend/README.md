# Frontend (React + Vite)

This folder contains the React frontend built with Vite. It shows collected reviews and connects to the backend API.

## Prerequisites
- Node.js 16+ and npm (or Yarn)

## Install

```bash
cd frontend
npm install
```

## Development

Start the dev server (hot reload):

```bash
npm run dev
```

The dev server will typically be available at `http://localhost:5173` (or the port Vite reports).

## Build

Build a production bundle:

```bash
npm run build
```

Preview the production build locally:

```bash
npm run preview
```

## Docker / Production
The project root includes `docker-compose.yml` which builds a production image for the frontend and serves it in a container. To run with Docker Compose:

```bash
docker-compose up --build
```

Access the frontend at `http://localhost:5173`.

## Notes
- If the frontend needs to talk to the backend API on a different host/port during development, update the API base URL in `src/api.js`.

Questions? I can add a `.env` sample or configure CORS settings on the backend to match your dev setup.
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
