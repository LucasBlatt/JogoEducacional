import cx_Freeze
executables = [cx_Freeze.Executable(
    script="JogoEducacional.py", icon="assets/icone.ico")]

cx_Freeze.setup(
    name="Junk Food Runner",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)