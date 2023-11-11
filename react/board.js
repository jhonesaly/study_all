const handleGetData = async () => {
    const userData = await fetch(`https://api.github.com/users/${user}`);
    const responseBody = await userData.text(); // Salvar o corpo da resposta como texto
//    const newUser = JSON.parse(responseBody); // Analisar o corpo como JSON
    
    console.log("user:", user);
    console.log("userData (text):", responseBody);
    //console.log("newUser (JSON):", newUser);
    

    if(newUser.name){
      const { avatar_url, name, bio, login } = newUser;
      //setGitUser({avatar_url, name, bio, login});

      const reposData = await fetch(`https://api.github.com/users/${user}/repos`);
      const newRepos = await reposData.json();

      if (newRepos.length){
        //setRepos(newRepos);
      }
    }
  };

var user = 'jhonesaly'
handleGetData()
