const firebaseConfig = {
  apiKey: "AIzaSyCANIJZfTSm2WeEaFB7-xfr_c8Mq82RlFE",
   authDomain: "lms-meta.firebaseapp.com",
    databaseURL: "https://lms-meta-default-rtdb.firebaseio.com",
    projectId: "lms-meta",
    storageBucket: "lms-meta.appspot.com",
    messagingSenderId: "506180671325",
    appId: "1:506180671325:web:3d6493c4a98b40d2377ab4",
    measurementId: "G-1V6XPL129Y"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
