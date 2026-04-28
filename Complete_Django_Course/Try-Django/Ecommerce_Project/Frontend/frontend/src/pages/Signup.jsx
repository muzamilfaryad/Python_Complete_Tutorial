import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Signup() {
  const BASE = import.meta.env.VITE_DJANGO_BASE_URL;
  const [form, setForm] = useState({ username: "", email: "", password: "", password2: "" });
  const [msg, setMsg] = useState("");
  const nav = useNavigate();

  const handleChange = e => setForm({...form, [e.target.name]: e.target.value});

  const handleSubmit = async e => {
    e.preventDefault();
    setMsg("");
    try {
      const res = await fetch(`${BASE}/api/register/`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(form)
      });
      const data = await res.json();
      if(res.ok) {
        setMsg("Account created. Redirecting to login...");
        setTimeout(()=>nav("/login"), 1200);
      } else {
        setMsg(data.username || data.password || JSON.stringify(data));
      }
    } catch(err) {
      console.error(err);
      setMsg("Signup failed");
    }
  };

  return (
    <div className="min-h-screen px-5 pb-10 pt-24 md:px-8">
      <div className="mx-auto w-full max-w-md rounded-3xl border border-orange-100 bg-white/90 p-7 shadow-xl md:p-8">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-orange-700">Join the experience</p>
        <h2 className="mb-4 mt-2 text-4xl font-bold text-stone-900">Create account</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input name="username" onChange={handleChange} value={form.username} placeholder="Username" required className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <input name="email" type="email" onChange={handleChange} value={form.email} placeholder="Email address" className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <input name="password" type="password" onChange={handleChange} value={form.password} placeholder="Password" required className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <input name="password2" type="password" onChange={handleChange} value={form.password2} placeholder="Confirm password" required className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <button className="w-full rounded-xl bg-stone-900 py-3 text-sm font-semibold text-white transition hover:bg-black md:text-base">Create account</button>
        </form>
        {msg && <p className="mt-3 text-sm text-stone-700">{msg}</p>}
        <p className="mt-5 text-sm text-stone-600">
          Already have an account?{" "}
          <Link to="/login" className="font-semibold text-orange-700 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Signup;