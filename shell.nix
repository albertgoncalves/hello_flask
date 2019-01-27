{ pkgs ? import <nixpkgs> {} }:
with pkgs; mkShell {
    name = "Flask";
    buildInputs = [ python36
                    python36.pkgs.flask
                    python36.pkgs.pillow
                    python36.pkgs.qrcode
                    python36.pkgs.sqlalchemy
                    python36.pkgs.flake8
                    sqlite
                    fzf
                  ];

    shellHook = ''
        if [ $(uname -s) = "Darwin" ]; then
            alias ls='ls --color=auto'
            alias ll='ls -al'
        fi

        alias flake8="flake8 --ignore E124,E128,E201,E203,E241,W503"
    '';
}
