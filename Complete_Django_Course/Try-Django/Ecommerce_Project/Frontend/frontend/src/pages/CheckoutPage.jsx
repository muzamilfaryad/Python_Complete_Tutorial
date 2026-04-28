import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { authFetch } from "../utils/auth";
import { useCart } from "../context/CartContext";

function CheckoutPage() {
  const [form, setForm] = useState({
    name: "",
    address: "",
    phone: "",
    payment_method: "COD",
  });

  const nav = useNavigate();
  const { clearCart } = useCart();
  const BASEURL = import.meta.env.VITE_DJANGO_BASE_URL;

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await authFetch(`${BASEURL}/api/orders/create/`, {
        method: "POST",
        body: JSON.stringify(form),
      });

      const data = await res.json();

      if (res.ok) {
        clearCart();
        alert("Order placed successfully!");
        nav("/");
      } else {
        alert(data.error || "Order failed");
      }
    } catch (error) {
      console.error("Checkout error:", error);
    }
  };

  return (
    <div className="min-h-screen px-5 pb-12 pt-24 md:px-8">
      <div className="mx-auto max-w-2xl rounded-3xl border border-orange-100 bg-white/90 p-6 shadow-xl md:p-8">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-orange-700">Secure checkout</p>
        <h1 className="mb-2 mt-2 text-4xl font-bold text-stone-900">Complete your order</h1>
        <p className="mb-6 text-sm text-stone-600">
          Fill your details once and we will handle the rest with smooth delivery updates.
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            name="name"
            value={form.name}
            onChange={handleChange}
            placeholder="Full name"
            required
            className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"
          />

          <input
            name="address"
            value={form.address}
            onChange={handleChange}
            placeholder="Shipping address"
            required
            className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"
          />

          <input
            name="phone"
            value={form.phone}
            onChange={handleChange}
            placeholder="Phone number"
            required
            className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"
          />

          <select
            name="payment_method"
            value={form.payment_method}
            onChange={handleChange}
            className="w-full rounded-xl border border-orange-200 bg-white p-3 outline-none transition focus:border-orange-400"
          >
            <option value="COD">Cash on delivery</option>
            <option value="ONLINE">Online payment</option>
          </select>

          <button className="w-full rounded-xl bg-stone-900 py-3 text-sm font-semibold text-white transition hover:bg-black md:text-base">
            Place order now
          </button>
        </form>
      </div>
    </div>
  );
}

export default CheckoutPage;