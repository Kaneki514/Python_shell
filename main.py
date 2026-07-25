import os
from init import Init
from Commands import Commands

class Main(Init, Commands):
    def __init__(self):
        Init.__init__(self)
        Commands.__init__(self)
        self.Running = True
        
    def Validate(self, cmd):
        cmd = cmd.strip()
        
        if not cmd:
            return
            
        parts = cmd.split(maxsplit=1)
        command  = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ''
        
        if command == '--help':
            self.help()
            return
            
        if command in self.commands:
            try:
                method = self.commands[command]
                
                if command == 'cd':
                    method(args)
                elif command == 'ls':
                    method(arg=args)
                elif command == 'pwd':
                    method(args)
                elif command == 'mkdir':
                    method(args)
                elif command == 'touch':
                    method(args)    
                else:
                    method()
            except (FileExistsError, OSError, NameError)as e:
                print(f'error ejecutando {command}: {e}')                    
        else:
            print(f"comando no enconstrado {command}")
            print("escribe --help para ver los comandos disponibles")
            
        
    def main(self):
        while self.Running:
            cmd = input('python@shell-$')
            self.Validate(cmd)
            
            
                 
        
        
if __name__ == "__main__":
    main = Main()
    main.main()
    exit(0)
