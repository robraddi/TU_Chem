# Miscellaneous 


## What is a Jupyter Notebook?

[Scientific_Comp_JupyterNotebook.ipynb](https://github.com/robraddi/TU_Chem/blob/master/Miscellaneous/Scientific_Comp_JupyterNotebook.ipynb)  is a notebook that I presented in a course during my undergraduate career to introduce python and Jupyter Notebooks.


## Python Lessons

[Python_Lessons.ipynb](https://github.com/robraddi/TU_Chem/blob/master/Miscellaneous/Python_Lessons.ipynb)

## Markdown

[Intro_to_Markdown.ipynb](https://github.com/robraddi/TU_Chem/blob/master/Miscellaneous/Intro_to_Markdown.ipynb)


## [Port forward](https://en.wikipedia.org/wiki/Port_forwarding) Jupyter Notebooks
The goal here is to redirect the communication from the internal host to the destination IP address and port number.  Ultimately, we are able to open/edit/write Jupyter Notebooks that are stored at a remote location by port forwarding to our local computer. Let's see how this works:

```bash
# Firstly, on the remote computer we need to specify that we don't want a browser to open when calling Jupyter. We also need to specify a port number.
## Remote terminal:
Jupyter notebook --no-browser --port=8889  

# Then, on the local computer we need to secure a connection with the remote location specifying the port number of the remote and the local followed by your username@hostname.
# e.g., ssh -N -f -L localhost:[remote port #]:localhost:[local port #] username@hostname  
## Local terminal:
ssh -N -f -L localhost:8889:localhost:8888 tuc41004@vav6.chem.temple.edu  

# Finally, open a browser on your local machine and type: localhost:[local port #] e.g., localhost:8888

---------------------------------------------------------------------------------------------------------------------------------
# NOTE: (IF python 2)
# Enter in the token from the remote terminal inside the prompt on your local browser. 
example:

[I 08:47:55.211 NotebookApp] Writing notebook server cookie secret to /run/user/21006/jupyter/notebook_cookie_secret
[I 08:48:01.859 NotebookApp] JupyterLab beta preview extension loaded from /home/...
[I 08:48:01.859 NotebookApp] JupyterLab application directory is /home/tuc41004/anaconda2/share/jupyter/lab
[I 08:48:01.906 NotebookApp] Serving notebooks from local directory: /home/tuc41004
[I 08:48:01.906 NotebookApp] 0 active kernels
[I 08:48:01.906 NotebookApp] The Jupyter Notebook is running at:
[I 08:48:01.907 NotebookApp] http://localhost:8888/?token=2fb1f102fdb595adba129862ce35sdavadsgv5347661efa1f050
[I 08:48:01.907 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 08:48:01.907 NotebookApp] No web browser found: could not locate runnable browser.
[C 08:48:01.908 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=2fb1f102fdb595adba1298dfvufnbo8rwtn95347661efa1f050&token=2fb1f102wefqwegfqrg5e6uce35455495347661efa1f050

```










