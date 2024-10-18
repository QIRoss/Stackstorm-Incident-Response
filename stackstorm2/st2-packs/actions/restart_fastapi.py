from st2common.runners.base_action import Action
import docker

class RestartFastAPI(Action):
    def run(self):
        client = docker.from_env()

        try:
            container = client.containers.get("fastapi")
            if container.status != "running":
                container.stop()
                container.remove()

                client.containers.run("tiangolo/uvicorn-gunicorn-fastapi:python3.8", name="fastapi1", detach=True, ports={'80/tcp': 8001})
                client.containers.run("tiangolo/uvicorn-gunicorn-fastapi:python3.8", name="fastapi2", detach=True, ports={'80/tcp': 8002})
                return True
            else:
                return False
        except docker.errors.NotFound:
            client.containers.run("tiangolo/uvicorn-gunicorn-fastapi:python3.8", name="fastapi1", detach=True, ports={'80/tcp': 8001})
            client.containers.run("tiangolo/uvicorn-gunicorn-fastapi:python3.8", name="fastapi2", detach=True, ports={'80/tcp': 8002})
            return True
