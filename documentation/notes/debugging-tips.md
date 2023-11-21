# DEBUGGING TIPS

    call in code: debugpy.breakpoint()

    In launch.json
    ###############

    "autoReload" : "enable"
    
    Note: When the debugger performs a reload, code that runs on import might be executed again. 
    To avoid this situation, try to only use imports, constants, and definitions in your module, 
    placing all code into functions. 

    Alternatively, you can also use if __name__=="__main__" checks.
