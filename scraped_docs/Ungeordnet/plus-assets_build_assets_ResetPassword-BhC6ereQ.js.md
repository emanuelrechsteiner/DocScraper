---
url: https://tailwindcss.com/plus-assets/build/assets/ResetPassword-BhC6ereQ.js
scraped_at: 2025-05-25T09:00:03.258188
title: Untitled
---

```
import{v as p,j as e}from"./app-DTQH4UGu.js";import{H as u,B as c}from"./Head-D_rlIIUW.js";import{T as o}from"./Forms-DJpII6st.js";import{h as w}from"./Layout-D3hTlOaQ.js";import"./client-wzkQ7pOV.js";import"./switch-_Jbw3XT6.js";function b({token:i,email:l}){const{data:t,setData:a,post:m,processing:d,errors:r}=p({token:i,email:l,password:""});function n(s){s.preventDefault(),m(s.target.action)}return e.jsxs(e.Fragment,{children:[e.jsx(u,{title:"Reset Password"}),e.jsxs(w,{children:[e.jsx("h1",{className:"text-sm/6 font-semibold",children:"Reset your password"}),e.jsx("p",{className:"mt-4 text-sm/6 text-gray-600",children:"Enter your email and the new password you'd like to use to access your account."}),e.jsxs("form",{className:"mt-10",onSubmit:n,action:"/plus/password/reset",children:[e.jsx(o,{label:"Email",id:"email",type:"email",error:r.email,value:t.email,onChange:s=>a("email",s.target.value),required:!0}),e.jsx(o,{className:"mt-6",label:"New password",id:"new-password",type:"password",error:r.password,value:t.password,onChange:s=>a("password",s.target.value),autoComplete:"new-password",required:!0}),e.jsx(c,{className:"mt-10 w-full",type:"submit",disabled:d,children:"Update password"})]})]})]})}export{b as default};

```


