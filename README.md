# 🧰 Taller práctico de Git (2 horas) — Guía paso a paso

Este README es el guion para nuestra clase. Lo seguiremos **en vivo** y cada estudiante ejecutará los comandos **en su propio equipo** mientras trabajamos en **un mismo repositorio** compartido.

> **Objetivo:** que al finalizar todos puedan **clonar**, **crear ramas**, **hacer commits**, **resolver conflictos**, **enviar PRs** y **hacer merge** con confianza.

---

## 🗓️ Agenda sugerida (120 min)

1. **(10 min)** Instalación y configuración inicial  
2. **(10 min)** Creación del repo remoto y clonación  
3. **(20 min)** Flujo básico: add → commit → push → pull  
4. **(15 min)** Trabajo con ramas (feature branches)  
5. **(20 min)** Pull Requests y revisión de código  
6. **(25 min)** Conflictos de merge (simulación y resolución)  
7. **(10 min)** `.gitignore`, mensajes de commit y buenas prácticas  
8. **(10 min)** Deshacer (reset, revert, restore) y tips finales

> Trae: Git instalado, cuenta en GitHub (o GitLab/Bitbucket), un editor (VS Code recomendado).

---

## 1) Instalación y configuración inicial

### 1.1 Instalar Git
- **Windows:** [gitforwindows.org](https://gitforwindows.org) (incluye Git Bash)
- **macOS:** `brew install git` (o Xcode Command Line Tools)
- **Linux (Debian/Ubuntu):** `sudo apt-get update && sudo apt-get install -y git`

Verifica:
```bash
git --version
```

### 1.2 Configurar identidad y editor
> **IMPORTANTE:** estos datos quedan en los metadatos de cada commit.

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@example.com"
git config --global core.editor "code --wait"   # VS Code
git config --global init.defaultBranch main
```

Ver ajustes:
```bash
git config --list
```

---

## 2) Acceso al remoto (GitHub) y autenticación

### 2.1 Opción A — HTTPS (más simple)
- Recomendado si no quieres configurar claves.  
- Cuando hagas `git push`, Git pedirá token/credenciales (en GitHub debes crear un **Personal Access Token** con permisos repo si te lo pide).

### 2.2 Opción B — SSH (recomendado a mediano plazo)
1. Genera una llave:
   ```bash
   ssh-keygen -t ed25519 -C "tu_email@example.com"
   # Enter para aceptar ruta por defecto, y opcionalmente pon passphrase
   ```
2. Muestra tu clave pública:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
3. Copia y pega en GitHub → Settings → SSH and GPG keys → New SSH key.  
4. Prueba:
   ```bash
   ssh -T git@github.com
   # Deberías ver "Hi <usuario>! You've successfully authenticated…"
   ```

---

## 3) Crear el repositorio remoto (por el profe) y clonar

1. El profe crea un repo en GitHub, por ejemplo: `org-curso/taller-git`.
2. Los estudiantes lo clonan (HTTPS o SSH):

```bash
# HTTPS
git clone https://github.com/org-curso/taller-git.git

# SSH
git clone git@github.com:org-curso/taller-git.git
```

3. Entra al directorio:
```bash
cd taller-git
```

> Si el repo viene vacío, inicia con un README y `.gitignore` (opcional):
```bash
echo "# Taller Git" > README.md
echo ".DS_Store" >> .gitignore   # macOS
echo "venv/" >> .gitignore       # Python (ejemplo)
git add .
git commit -m "chore: inicializa repo con README y .gitignore"
git push origin main
```

---

## 4) Flujo básico de trabajo (local)

### 4.1 Estado y preparación
```bash
git status         # qué cambió
git add <archivo>  # preparar archivo
git add .          # preparar todo (úsalo con cuidado)
```

### 4.2 Confirmar cambios
```bash
git commit -m "feat: agrega sección de instalación"
```
> Consejo: usa mensajes tipo conventional commits (`feat`, `fix`, `chore`, `docs`, `refactor`, etc.)

### 4.3 Enviar y traer cambios
```bash
git push origin main   # subir al remoto
git pull origin main   # traer cambios del remoto a local
```

---

## 5) Ramas (branching) y trabajo aislado

> **Idea:** cada estudiante crea una **rama con su nombre** y trabaja ahí.

### 5.1 Crear y cambiar de rama
```bash
git checkout -b feat/tu-nombre-perfil
# Edita un archivo o crea uno nuevo, p. ej. perfiles/tu-nombre.md
git add perfiles/tu-nombre.md
git commit -m "feat: agrega perfil de Tu Nombre"
git push -u origin feat/tu-nombre-perfil
```

### 5.2 Ver ramas
```bash
git branch        # locales
git branch -r     # remotas
git switch main   # cambiar de rama (alternativa a checkout)
```

---

## 6) Pull Requests (PR) y revisión

1. Sube tu rama (`git push -u origin <rama>`).
2. En GitHub → **Compare & pull request**.
3. Asigna revisores, describe el cambio (qué, por qué, cómo probar).
4. **No** merges locales a `main`. Usamos PRs para integrar.

**Opcional (mantener rama actualizada con main):**
```bash
git fetch origin
git switch <tu-rama>
git merge origin/main     # o git rebase origin/main (si ya dominás rebase)
```

---

## 7) Simulación de conflictos y cómo resolverlos

> **Ejercicio en clase:** Dos personas editan la **misma línea** en `equipo.md`.

### 7.1 Reproducir conflicto
- Persona A edita línea 5 → commit → push.
- Persona B edita *también* la línea 5 → commit → intenta `git push` → **rechazado**.
- Persona B hace:
  ```bash
  git pull origin main
  ```
  Git puede decir: *Merge conflict in equipo.md*.

### 7.2 Resolver
1. Abre el archivo con conflicto: verás marcas como:
   ```
   <<<<<<< HEAD
   (tu versión)
   =======
   (versión remota)
   >>>>>>> origin/main
   ```
2. **Edita** para dejar la versión final correcta.
3. Marca como resuelto y confirma:
   ```bash
   git add equipo.md
   git commit -m "fix: resuelve conflicto en equipo.md"
   git push origin main   # o en tu rama si estabas ahí
   ```

> **Tip:** VS Code ayuda visualmente a “Aceptar cambios entrantes/actuales/ambos”.

---

## 8) `.gitignore` y estructura del proyecto

### 8.1 Ignorar archivos que no deben versionarse
Ejemplos comunes:
```
# Sistema
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
venv/
.env

# Node
node_modules/
dist/
```
Guárdalo como `.gitignore` en la raíz:
```bash
git add .gitignore
git commit -m "chore: agrega .gitignore base"
git push
```

### 8.2 Propuesta de estructura (ejemplo)
```
taller-git/
├─ README.md
├─ .gitignore
├─ ejercicios/
│  ├─ ejercicio-01.md
│  └─ ejercicio-02.md
└─ perfiles/
   ├─ tu-nombre.md
   └─ ...
```

---

## 9) Ver historial y comparar

```bash
git log --oneline --graph --decorate --all
git show <hash>                 # detalles de un commit
git diff                        # diferencias sin preparar
git diff --staged               # diferencias preparadas (index)
git blame <archivo>             # quién tocó cada línea (auditoría)
```

---

## 10) Deshacer: restore, reset, revert (cuándo usar cada uno)

- **Descartar cambios sin preparar:**
  ```bash
  git restore <archivo>
  ```
- **Sacar un archivo del área de preparación (unstage):**
  ```bash
  git restore --staged <archivo>
  ```
- **Volver a un commit anterior moviendo la rama (historial local):**
  ```bash
  git reset --hard <hash>
  ```
  > ⚠️ Peligroso si ya lo subiste a remoto. Evítalo en `main` compartida.

- **Crear un commit que “deshace” otro (seguro en remoto):**
  ```bash
  git revert <hash>
  ```

- **Guardar cambios temporales (sin commitear):**
  ```bash
  git stash
  git stash list
  git stash pop
  ```

> **Regla de oro:** en ramas compartidas (`main`) **prefiere `revert`**. Usa `reset --hard` solo en tu rama local y sabiendo lo que haces.

---

## 11) Buenas prácticas rápidas

- **Commits pequeños y frecuentes** con mensajes claros.  
- **Ramas por funcionalidad**: `feat/…`, `fix/…`, `docs/…`  
- **No commits en `main`**: usa PRs y revisiones.  
- **Actualiza tu rama** antes de abrir PR (reduce conflictos).  
- **Incluye `.gitignore`** desde el inicio.  
- Revisa cambios antes de commitear: `git status`, `git diff`.

---

## 12) Mini-ejercicios en tiempo real (para esta clase)

1. **Config inicial**: `git config --global …`  
2. **Clonar** el repo del curso.  
3. **Crear rama personal**: `git checkout -b feat/tu-nombre-perfil`  
4. **Agregar tu perfil** en `perfiles/<tu-nombre>.md`, commit y push.  
5. **Crear PR** y solicitar revisión.  
6. **Resolver un conflicto** simulado en `equipo.md`.  
7. **Practicar revert** de un commit de prueba.  
8. **Agregar `.gitignore`** (si no existe) y **limpiar** archivos no deseados.

---

## 13) Problemas comunes (y cómo salir)

- **“Authentication failed” (HTTPS):** crea/usa un **Personal Access Token** y usa eso como contraseña al hacer `push`.  
- **“Permission denied (publickey)” (SSH):** agrega tu **SSH key** a GitHub y prueba `ssh -T git@github.com`.  
- **“non-fast-forward” al hacer push:** primero `git pull --rebase origin main` (o `merge`), resuelve conflictos y vuelve a `push`.  
- **Subí archivos que no debía:** añádelos a `.gitignore` y `git rm --cached <archivo>` → commit → push.  
- **Me quedé “pegado” en merge:** `git merge --abort` para volver atrás y reintentar (o pide ayuda).

---

## 14) Glosario mínimo

- **Repositorio:** carpeta versionada por Git.  
- **Commit:** “foto” de los cambios con un mensaje.  
- **Branch (rama):** línea de trabajo independiente.  
- **Merge:** integrar ramas.  
- **Pull Request:** propuesta de integración con revisión.  
- **Remote (origin):** copia alojada en servidor (GitHub).  
- **HEAD:** puntero a tu commit/branch actual.  
- **Staging area (index):** zona intermedia antes del commit.

---

## 15) Referencias útiles

- [Git Book (gratis)](https://git-scm.com/book/en/v2)  
- [GitHub Docs](https://docs.github.com/)  
- [Cheat Sheet de Git](https://training.github.com/)

---

## ✅ Checklist final para hoy

- [ ] Configuré mi usuario y editor.  
- [ ] Cloné el repo del curso.  
- [ ] Creé y empujé mi rama personal.  
- [ ] Abrí un PR con mi aporte.  
- [ ] Practiqué resolución de conflictos.  
- [ ] Entendí cómo revertir y resetear.  
- [ ] Dejé mi `.gitignore` listo.

¡Listo! Con esto, estás trabajando como un pro con Git. 🚀
