import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { saveTokens } from "../utils/auth";

function Login() {
  const BASE = import.meta.env.VITE_DJANGO_BASE_URL;
  const [form, setForm] = useState({ username: "", password: "" });
  const [msg, setMsg] = useState("");
  const nav = useNavigate();

  const handleChange = e => setForm({...form, [e.target.name]: e.target.value});

  const handleSubmit = async e => {
    e.preventDefault();
    setMsg("");
    try {
      const res = await fetch(`${BASE}/api/token/`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(form),
      });
      const data = await res.json();
      if (res.ok) {
        saveTokens(data);
        setMsg("Login successful!");
        setTimeout(()=>nav("/"), 800);
      } else {
        setMsg(data.detail || "Invalid credentials");
      }
    } catch(err) {
      console.error(err);
      setMsg("Login failed");
    }
  };

  return (
    <div className="min-h-screen px-5 pb-10 pt-24 md:px-8">
      <div className="mx-auto w-full max-w-md rounded-3xl border border-orange-100 bg-white/90 p-7 shadow-xl md:p-8">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-orange-700">Welcome back</p>
        <h2 className="mb-4 mt-2 text-4xl font-bold text-stone-900">Sign in</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input name="username" onChange={handleChange} value={form.username} placeholder="Username" required className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <input name="password" type="password" onChange={handleChange} value={form.password} placeholder="Password" required className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"/>
          <button className="w-full rounded-xl bg-stone-900 py-3 text-sm font-semibold text-white transition hover:bg-black md:text-base">Continue</button>
        </form>
        {msg && <p className="mt-3 text-sm text-stone-700">{msg}</p>}
        <div className="mt-5 text-sm text-stone-600">
          New here?{" "}
          <Link to="/signup" className="font-semibold text-orange-700 hover:underline">
            Create your account
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Login;