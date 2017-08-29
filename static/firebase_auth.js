/*
 * firebase_auth.js
 * ----------------------
 * Carries out the authentication process with firebase before passing the details off to our backend
 * Created by: Peter Richards (28/08/17)
 */

//Define login providers
var firebase_auth_provider_facebook = new firebase.auth.FacebookAuthProvider();
var firebase_auth_provider_google = new firebase.auth.GoogleAuthProvider();
var firebase_auth_notice = document.querySelector('.firebase_auth_notice');

//Authenticate the credentials with firebase
function firebase_authenticate(firebase_provider){
  //Tell the user we're working on it
  firebase_auth_notice.innerHTML = "Please Wait.";
  firebase_auth_notice.classList.add('firebase_auth_notice_visible');
  //Switch between the different providers to find the correct process
  if(firebase_provider === 'email'){
    //Process as an email & password login
    var form = document.querySelector('form');
    firebase.auth().signInWithEmailAndPassword(form.querySelector('input[type=email]').value, form.querySelector('input[type=password]').value).catch(function(error){firebase_auth_notice.innerHTML = error.message;firebase_auth_notice.classList.add('firebase_auth_notice_visible');});
  }else{
    //Make sure that if we're at this stage it's either google or facebook, kick anything else out.
    if(firebase_provider === 'google'){firebase_provider = firebase_auth_provider_google;}else if(firebase_provider === 'facebook'){firebase_provider = firebase_auth_provider_facebook;}else{firebase_auth_notice.innerHTML = "Unknown login error.";firebase_auth_notice.classList.add('firebase_auth_notice_visible');return;}
    //Open the appropriate pop up for the provider
    firebase.auth().signInWithPopup(firebase_provider).catch(function(error){firebase_auth_notice.innerHTML = error.message;firebase_auth_notice.classList.add('firebase_auth_notice_visible');});
  }
  //Once this has finished, return. From here we wait for firebase to change the auth status which we pick up in the next function
}

//Check for a change in the authentication state & send off to the backend
firebase.auth().onAuthStateChanged(function(user) {
  //Make sure that a user has been set, we don't want to be sending logouts
  if(user){user.getIdToken().then(function(firebase_auth_token){
    //Create a hidden element in the form, add the token
    var firebase_auth_form_element = document.querySelector('form');var firebase_auth_token_element = document.createElement('input');
    firebase_auth_token_element.setAttribute('type', 'hidden');firebase_auth_token_element.setAttribute('name', 'auth_token');firebase_auth_token_element.setAttribute('value', firebase_auth_token);
    firebase_auth_form_element.appendChild(firebase_auth_token_element);
    //Log the user out of firebase's backend, we don't need it anymore, then submit the form after a short 5 second delay to prevent google's future weirdness that sometimes happens
    firebase.auth().signOut();
    setTimeout(function(){firebase_auth_form_element.submit();}, 5000);
  });}
});
