# Docker Image For [BookStack](https://github.com/ssddanbrown/BookStack)

## How to use the Image without Docker compose

*(For Docker 1.9+)*

1. Create a shared network:

```bash
docker network create bookstack_nw
```

2. Run MySQL container :

```bash
docker run -d --net bookstack_nw  \
-e MYSQL_ROOT_PASSWORD=secret \
-e MYSQL_DATABASE=bookstack \
-e MYSQL_USER=bookstack \
-e MYSQL_PASSWORD=secret \
 --name="bookstack_db" \
 mysql:8
```

3. Run BookStack Container

```bash
docker run -d --net bookstack_nw \
-e DB_HOST=bookstack_db:3306 \
-e DB_DATABASE=bookstack \
-e DB_USERNAME=bookstack \
-e DB_PASSWORD=secret \
-e APP_URL=http://example.com \
-p 8080:8080 \
--name="bookstack_22.10.1" \
 ghcr.io/codemicro/bookstack:22.10.1
```

The APP_URL parameter should be the base URL for your BookStack instance without a trailing slash. For example:
APP_URL=http://example.com

### Volumes
To access your `.env` file and important bookstack folders on your host system change `<HOST>` in the following line to your host directory and add it then to your run command:

```bash
--mount type=bind,source=<HOST>/.env,target=/var/www/bookstack/.env \
-v <HOST>:/var/www/bookstack/public/uploads \
-v <HOST>:/var/www/bookstack/storage/uploads
```
In case of a windows host machine the .env file has to be already created in the host directory otherwise a folder named .env will be created.

After these steps you can visit [http://localhost:8080](http://localhost:8080). You can login with username 'admin@admin.com' and password 'password'.

## Extras

* Includes a copy of [Mathjax 3](https://www.mathjax.org) at `/libs/mathjax/tex-chtml-full.js`

  This can be used with the following snippet that can be placed in the custom HTML head content section in your Bookstack settings in order to enable LaTeX support.
  ```html
  <script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$']]
    }
  };
  </script>
  <script id="MathJax-script" async
    src="/libs/mathjax/tex-chtml-full.js">
  </script>
  ```

## Inspiration

This is a fork of [solidnerd/docker-bookstack](https://github.com/solidnerd/docker-bookstack), which is in turn a fork of [Kilhog/docker-bookstack](https://github.com/Kilhog/docker-bookstack). Kilhog did the intial work, solidnerd wanted to go in a different direction and I wanted an up-to-date version of the image.
