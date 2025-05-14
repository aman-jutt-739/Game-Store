// import React, { useState } from 'react';
// import styles from './Login.module.css'; // new CSS
// import { useNavigate } from 'react-router-dom';
// import { motion } from 'framer-motion';

// const Login = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const navigate = useNavigate();

//   const handleLogin = async () => {
//     const response = await fetch("http://localhost:5000/api/login", {
//       method: 'POST',
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ email, password })
//     });

//     const data = await response.json();
//     if (response.ok) {
//       alert("Login successful");
//       navigate('/browse');
//     } else {
//       alert(data.error || "Login failed");
//     }
//   };

//   return (
//     <div className={styles.main}>
//     {overlap ? 
//         <motion.div 
//           className={styles.overlap}
//           variants={buttonVariants}
//           initial="hidden"
//           animate="visible"
//         >
  
//         </motion.div> 
//     : null}

//     {cartDisplayed ? <Cart 
//             cartDisplayed={cartDisplayed} 
//             handleOpenCart={handleOpenCart}
//             handleCloseCart={handleCloseCart}
//             cart={cart}
//             cartAmount={cartAmount}
//             handleHover={handleHover}
//             hoverState={hoverState}
//             clearCart={clearCart}
//             handleRemoveFromCart={handleRemoveFromCart}
//             openGamePage={openGamePage}
//     /> : null}
//       <div className={styles.home}>

//               <video autoPlay muted loop className={styles.video}>
//                 <source src={require("../../Resources/image/video.mp4")} type="video/mp4" />
//               </video>

//               <NavBar 
//                 handleHover={handleHover} 
//                 hoverState={hoverState}
//                 browsing={browsing}
//                 handleBrowse={handleBrowse}
//                 handleHome={handleHome}
//                 landingPage={landingPage}
//                 cartAmount={cartAmount}
//                 handleOpenCart={handleOpenCart}
//                 handleCloseCart={handleCloseCart}
//               />
//               <div className={styles.container}>
//                   <div className={styles.left}>
//                       <div className={styles.splash}>
//                         <h1>Welcome Back</h1>
//                         <p className={styles.intro}>A Full Stack Web Application using React and Flask. Developed by Ahmad Naeem and Aman Khurram under the supervision of Mr. Talha Arif.</p>
//                       </div>
  
//                       <div className={styles.buttons}>
//                             <button className={`${styles.cta} ${styles.browseBtn}`} onClick={handleBrowse} aria-label="Browse">
//                               <Enter className={styles.ctaSVG} />
//                               Browse
//                             </button>
                           
//                             {/* <a href="https://github.com/gianlucajahn" target="_blank"><button className={styles.cta} aria-label="View Repository">
//                               <GitHubLogo className={styles.ctaSVG} />
//                               GitHub
//                             </button></a> */}
//                             <a href="https://www.linkedin.com/in/ahmad-naeem-17716228a/" target="_blank"><button className={`${styles.cta} ${styles.lastChild}`} aria-label="Open LinkedIn">
//                               <LinkedIn className={`${styles.ctaSVG} ${styles.linkedin}`} />
//                               <span>LinkedIn Ahmad</span>
//                             </button></a>
//                             <a href="https://www.linkedin.com/in/aman-khurram-117543297/" target="_blank"><button className={`${styles.cta} ${styles.lastChild}`} aria-label="Open LinkedIn">
//                               <LinkedIn className={`${styles.ctaSVG} ${styles.linkedin}`} />
//                               <span>LinkedIn Aman</span>
//                             </button></a>
                            
//                       </div>
//                   </div>
  
//               </div>
//       </div>
//   </div>
//     // <div className={styles.loginPage}>
//     //   {/* <video autoPlay muted loop className={styles.video}>
//     //     <source src={require("../../Resources/image/video.mp4")} type="video/mp4" />
//     //   </video> */}

//     //   <motion.div 
//     //     className={styles.loginBox}
//     //     initial={{ opacity: 0, y: 200 }}
//     //     animate={{ opacity: 1, y: 0 }}
//     //     transition={{ duration: 1 }}
//     //   >
//     //     <h1>Welcome Back</h1>
//     //     <p className={styles.subtitle}>Log in to continue</p>
//     //     <input 
//     //       type="text" 
//     //       placeholder="Email" 
//     //       value={email}
//     //       onChange={(e) => setEmail(e.target.value)}
//     //     />
//     //     <input 
//     //       type="password" 
//     //       placeholder="Password" 
//     //       value={password}
//     //       onChange={(e) => setPassword(e.target.value)}
//     //     />
//     //     <button className={styles.cta} onClick={handleLogin}>Log In</button>
//     //   </motion.div>
//     // </div>
//   );
// };

// export default Login;
