docker build -t 5g_conf_api .
docker run  -p 8000:8000 -v /home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/.env:/app/conf_files/.env -v  /var/run/docker.sock:/var/run/docker.sock 5g_conf_api:latest