# bashrc bash_profile

## .bashrc と .bash_profile の違い
読み込むフローとしては以下の 2 パターンがあるようだ

- .bashrc
- .bashrc → .bash_profile

でも 1 のパターンは bash コマンドを単独で打った時だけなので、普段は気にしなくて良さそう。

## .bashrcの再読み込み
sourceコマンドで。

source ~/.bashrc

## my bashrc

```
export PS1="$ "

export PS1="$ "
alias reload="source ~/.YOUR_BASHRC_NAME"
alias editme="vim ~/.YOUR_BASHRC_NAME"

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias ll='ls -l'
alias la='ls -a'

alias pscpu='ps awux | head -1; ps awux | sort -k3 -nr'
alias psmem='ps awux | head -1; ps awux | sort -k4 -nr'

# your shortcut comamnds...
alias cloc="/root/tools/cloc/cloc"
...
```
