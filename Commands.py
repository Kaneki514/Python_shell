import os

class Commands:
    def __init__(self):
        self.path_lists = []
        self.command_list = [
            "--help",
            "ls",
            "cd",
            "pwd",
            "mkdir",
            "touch",
            "exit"]
        self.commands = {
            'ls': self.ls,
            'cd': self.cd,
            'pwd': self.pwd,
            'mkdir': self.mkdir,
            '--help': self.help,
            'touch': self.touch,
            'exit': lambda:self.Running = False
        }
        
                
    #COMANDO --help
    
    def help(self):
        print('--help')
        print(f"""
Esto es una consola de comandos basada en shell the bash con comandos 
simples y utiles de los cuales disponibles ya están {self.command_list}        
        """)    
        
        
    #COMANDO LS    
        
    def ls(self, **args):
        
        if args['arg'] == '-a':
            print('ls -a')
            for i in os.listdir(os.getenv('PY_CURRENT_PATH')):
                print(i)
        
        elif args['arg'] == '':
            print('ls')
            for i in os.listdir(os.getenv('PY_CURRENT_PATH')):
                if i.startswith('.'):
                    pass
                else: 
                    print(i)
                    
        elif args['arg'] == '--help':
            print('ls --help')
            print(""""ls: muestra archivos y carpetas del directorio actual.
uso: ls <argumentos>
-a     > muestra todos los archivos (incluyendo ocultos)
--help > muestra este mensaje.
            """)            

        else:
            print('Error ls')
                    
                    
    #COMANDO CD                
        
    def cd(self, cd_path):
        cd_path = cd_path.strip()
        
        if not cd_path or cd_path == '--help':
            print("""cd: cambia el directorio actual
uso: cd <ruta>
..     > subir al directorio padre
/ruta/absoluta
ruta/relativa
--help > muestra esta ayuda""")
            return
        
        current = os.getenv('PY_CURRENT_PATH', '/')
        
        # Caso especial: cd ..
        if cd_path == '..':
            new_path = os.path.dirname(current.rstrip('/'))
            if new_path == '':
                new_path = '/'
            os.environ['PY_CURRENT_PATH'] = new_path
            print(new_path)
            return
        
        # Construir nueva ruta
        if os.path.isabs(cd_path):
            new_path = cd_path
        else:
            new_path = os.path.join(current, cd_path)
        
        # Normalizar y verificar
        new_path = os.path.abspath(new_path)
        
        if os.path.exists(new_path) and os.path.isdir(new_path):
            os.environ['PY_CURRENT_PATH'] = new_path
            print(new_path)
        else:
            print(f"cd: no existe el directorio: {cd_path}")

    def pwd(self, arg):
        if arg == '--help':
            print('pwd --help')
            print("Este comando muestra el directorio actual")
            
        else:
            print(os.getenv('PY_CURRENT_PATH'))    
            
    def mkdir(self, path_name):
        print(f'mkdir {path_name}')
        try:
           if os.path.isdir(os.path.join(os.getenv('PY_CURRENT_PATH'), path_name)):
               print("Carpeta ya existe")
           else:  
               os.mkdir(os.path.join(os.getenv('PY_CURRENT_PATH') ,path_name))
        except (OSError, FileExistsError) as e:
            print(f"Error: {e}")
            
    def touch(self, file_name):
        print(f'touch {file_name}')
        try:
            if os.path.isfile(os.path.join(os.getenv('PY_CURRENT_PATH'), file_name)):
                print("Archivo ya existe")
            else:    
                with open(os.path.join(os.getenv('PY_CURRENT_PATH') ,file_name), 'w') as file:
                    file.write('')
        except (OSError, FileExistsError) as e:
            print(f"Error: {e}")                    
        