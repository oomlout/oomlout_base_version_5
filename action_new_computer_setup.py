import os
import copy

### to look into adding github cli
#winget install --id GitHub.cli
#gh auth login

def main(**kwargs):
    print("action_new_computer_setup.py main()")
    
    git_long_directory = True
    pip = True
    path = True
    pythonpath = True
    clone = True
    
    git_long_directory = False
    pip = False
    path = False
    pythonpath = False
    #clone = False
    
    if git_long_directory: 
        print("doing all the git stuff")
        git_directory = "C:\\Users\\aaron\\AppData\\Local\\GitHubDesktop\\app-3.5.8\\resources\\app\\git\\cmd"
        os.system(f'cd /d "{git_directory}" && git config --system core.longpaths true')
        

    #run python_pip.bat
    if pip:     
        print("doing all the pip installs")   
        os.system("action_python_pip.bat")
        

    # environment_variable = "PATH"
    if path:
        print("doing all the path stuff")
        folder_path = []
        folder_path.append("c:\\gh\\oomlout_base_version_5") 
        #db path
        folder_path.append("c:\\od\\OneDrive\\path") 
        #oobb
        folder_path.append("c:\\gh\\oomlout_oobb_version_5")
        #oomp
        folder_path.append("c:\\gh\\oomlout_oomp_version_5")
        #inkscape
        folder_path.append("C:\\Program Files\\Inkscape\\bin")
        #ai_roboclick
        folder_path.append("C:\\gh\\oomlout_roboclick")
        

        kwargs["folder_path"] = folder_path
        set_folder_path(**kwargs)

    # environment_variable = "PYTHONPATH"
    if pythonpath:
        print("pythonpath()")   
        folder_pythonpath = []
        folder_pythonpath.append("c:\\gh\\oomlout_base_version_5")
        #oobb
        folder_pythonpath.append("c:\\gh\\oomlout_oobb_version_5")
        # oomp
        folder_pythonpath.append("c:\\gh\\oomlout_oomp_version_5")
        # ai_robo_click
        folder_pythonpath.append("C:\\gh\\oomlout_roboclick")
        kwargs["folder_pythonpath"] = folder_pythonpath
        set_folder_pythonpath(**kwargs)

    
    # clone repos
    if clone:
        file_oomlout_repos = "github_repos.yaml"

        kwargs["file_oomlout_repos"] = file_oomlout_repos
        clone_repos(**kwargs)


def clone_repos(**kwargs):
    file_oomlout_repos = kwargs["file_oomlout_repos"]

    #load the repos
    import yaml
    with open(file_oomlout_repos) as file:
        oomlout_repos = yaml.load(file, Loader=yaml.FullLoader)
    #loop through the repos
    for repo_id in oomlout_repos:
        repo = oomlout_repos[repo_id]        
        name = repo["name"]
        directory = repo.get("directory", "gh")
        directory = os.path.join("c:/", directory)
        url = repo.get("url", f"http://github.com/oomlout/{name}.git")
        repo_directory = os.path.join(directory, name)
        if os.path.exists(repo_directory):
            print(f"skipping {repo_directory}, already exists")
        else:
            os.makedirs(directory, exist_ok=True)
            os.system(f'git clone "{url}" "{repo_directory}"')


def install_programs(**kwargs):
    folder_base = "C:/od/OneDrive/install_files/install_files_new_computer"
    programs = []
    import glob
    #get all .exe from folder_base
    files = glob.glob(f"{folder_base}/*.exe")
    #add all .msi files
    files += glob.glob(f"{folder_base}/*.msi")
    for file in files:
        programs.append(file)


    for program in programs:
        choice = input(f"install {program}? (y/n)")
        if choice == "y":
            os.system(program)
        else:
            print(f"skipping {program}")

    


def set_folder_path(**kwargs):
    environment_variable = "PATH"
    kwargs["environment_variable"] = environment_variable
    set_folder_generic(**kwargs)

def set_folder_pythonpath(**kwargs):
    environment_variable = "PYTHONPATH"
    kwargs = copy.deepcopy(kwargs)
    kwargs["folder_path"] = kwargs["folder_pythonpath"]    
    kwargs["environment_variable"] = environment_variable
    set_folder_generic(**kwargs)

def set_folder_openscadpath(**kwargs):
    environment_variable = "OPENSCADPATH"
    kwargs = copy.deepcopy(kwargs)
    kwargs["folder_path"] = kwargs["folder_openscadpath"]    
    kwargs["environment_variable"] = environment_variable
    set_folder_generic(**kwargs)


def set_folder_generic(**kwargs):
    print("action_new_computer_setup.py set_folder_path()")
    folder_path = kwargs["folder_path"]
    environment_variable = kwargs.get("environment_variable", "PATH")    
    #print("folder: ", folder)
    #add folder to the path variable if it isn't already there using os.system it is windows

    path_current = os.environ.get(environment_variable, None)
    if path_current is None:
        os.environ[environment_variable] = ""
        path_current = os.environ[environment_variable]

    new_path = f'{path_current}'
    #split new path with ; and remove duplicates            
    new_path = new_path.split(";")
    new_path = list(set(new_path))
    #remove "" entries
    new_path = [x for x in new_path if x != ""]            
    for folder in folder_path:
        folder = folder.replace("/", "\\")
        # if fiolder not in any of new_path.lower()
        if not any(folder.lower() in s.lower() for s in new_path):
            new_path.append(folder)

    new_path = ";".join(new_path)
    new_path = new_path.replace("/", "\\")
    command = f'setx {environment_variable} "{new_path}"'
    os.system(command)
    # echo path using os.system
    #os.system(f'echo %PATH%')


    #print out the current path variable
    #path_current = os.environ['PATH']
    #print("path_current: ", path_current)


if __name__ == '__main__':
    main()

