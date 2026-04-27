import os
import copy
import subprocess

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
    #path = False
    pythonpath = False
    clone = False
    
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
        folder_path.append("c:\\gh\\oomlout_base_version_5\\path") 
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

    path_current = get_user_environment_variable(environment_variable)
    new_path = split_environment_paths(path_current)

    for folder in folder_path:
        folder = folder.replace("/", "\\")
        if not path_entry_exists(folder, new_path):
            new_path.append(folder)
            set_user_environment_variable(environment_variable, new_path)
            print(f"added {folder} to {environment_variable}")
        else:
            print(f"skipping {folder}, already in {environment_variable}")

    os.environ[environment_variable] = ";".join(new_path)


def split_environment_paths(path_value):
    if path_value is None:
        return []

    paths = []
    for path in path_value.split(";"):
        path = path.strip().replace("/", "\\")
        if path and not path_entry_exists(path, paths):
            paths.append(path)
    return paths


def path_entry_exists(folder, paths):
    folder = normalize_path_entry(folder)
    return any(folder == normalize_path_entry(path) for path in paths)


def normalize_path_entry(path):
    return path.strip().strip('"').replace("/", "\\").rstrip("\\").lower()


def get_user_environment_variable(environment_variable):
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        f"[Environment]::GetEnvironmentVariable('{environment_variable}', 'User')",
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout.strip()


def set_user_environment_variable(environment_variable, paths):
    path_value = ";".join(paths).replace("/", "\\")
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        (
            f"[Environment]::SetEnvironmentVariable("
            f"'{environment_variable}', "
            f"$env:OOMLOUT_ENVIRONMENT_VALUE, "
            f"'User')"
        ),
    ]
    env = os.environ.copy()
    env["OOMLOUT_ENVIRONMENT_VALUE"] = path_value
    subprocess.run(command, env=env, check=True)


if __name__ == '__main__':
    main()

