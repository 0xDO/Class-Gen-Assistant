# compound launch configuration

An alternative way to start multiple debug sessions is by using a compound launch configuration.  
A compound launch configuration lists the names of two or more launch configurations that should be launched in parallel.  
Optionally a preLaunchTask can be specified that is run before the individual debug sessions are started.  
The boolean flag stopAll controls whether manually terminating one session will stop all of the compound sessions.

    {
      "version": "0.2.0",  
      "configurations": [  
        {  
          "type": "node",  
          "request": "launch",  
          "name": "Server",  
          "program": "${workspaceFolder}/server.js"  
        },  
        {  
          "type": "node",  
          "request": "launch",  
          "name": "Client",  
          "program": "${workspaceFolder}/client.js"  
        }  
      ],  
      "compounds": [  
        {  
          "name": "Server/Client",  
          "configurations": ["Server", "Client"],  
          "preLaunchTask": "${defaultBuildTask}",  
          "stopAll": true  
        }  
      ]  
    }  
