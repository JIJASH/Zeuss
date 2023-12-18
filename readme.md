<!--yedi git first time setup gardai ho bhaney start chai yeta bata garam haii --->
git config --global user.email "....@gmail.com"
git config --global user.name "usr_name"

<!--to setup git in the project-->
git init

git status<!-- add garnu agi lets checkk>

<!-- to add files in git --->
git add .

<!-- to check status---k k xa git file bhitra,..k k add xa xaina dekhaunxa..--->
<!-- yedi git status garda red aaako xa bhaney thoose files are not in the git ...if green then yes-->
git status

<!--to commit after adding-->
git commit -m "somemessage to be printed in the console...k changed ho tyo message.."

<!-- k k changes haru gareko xa hamle ,...k k commit gareko xa bhanera yeuta thau ma store bhako hunxa ..to check it out--->
git log

<!--branch ko naam check out garna lai --->
git branch

<!-- by default chai github le hamro branch ko naam main bhanera banaunxa whereas git le chai master bhanera banaunxa..--->
<!--rename the current branch--->
git branch -M branch_ko_naam

<!--create new branch--generaally branch ko naam chai feature anusar banaunu parxa..jpaitei banayera chaldaina bhai..generally chai feature ho bhaney chai naam ko agadi feat bhanera haldinxa bug xa bhaney chai bug bhanera agdi haldinxa..issue xa bhaney issue bhanera haldinxa...natra overwrite ko problems aauna sakxa..--->
git checkout -b branch_ko_new_naam <!--git checkout -b feat_login>

<!---every branches are isolated of each other>

<!--to switch the branch from one another-->
git checkout kun_branch_ma_janey_tesko_naam

<!--jastai ma yeuta branch ma xu ra maile tyo branch ma basera arko yeuta branch banaye bhaney just tyo branch ko clone branch banney hoo..simply ma suruma bhako branch ma jj thyo newly creatd brance ma clone huney bhayo..and both of the branches are isolated..bhanna ley they are independent of each other ..yeuta ko updates and changes le arko lai kei problems gardaina...and soo on and onnnn-->

