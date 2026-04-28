import { Link, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useCart } from "../context/CartContext";

function ProductDetails() {
  const { id } = useParams();
  const BASEURL = import.meta.env.VITE_DJANGO_BASE_URL;
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { addToCart } = useCart();

  useEffect(() => {
    fetch(`${BASEURL}/api/products/${id}/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch product details");
        }
        return response.json();
      })
      .then((data) => {
        setProduct(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, [id, BASEURL]);

  if (loading) {
    return <div className="pt-32 text-center text-stone-700">Preparing product details...</div>;
  }
  if (error) {
    return <div className="pt-32 text-center text-red-700">Unable to load this product: {error}</div>;
  }
  if (!product) {
    return <div className="pt-32 text-center text-stone-700">No product found.</div>;
  }

  const handleAddToCart = () => {
    if(!localStorage.getItem('access_token')){
      window.location.href = '/login';
      return;
    }
    addToCart(product.id);
  }
  return (
    <div className="min-h-screen px-5 pb-12 pt-24 md:px-8">
      <div className="mx-auto max-w-6xl rounded-3xl border border-orange-100 bg-white/90 p-7 shadow-xl md:p-10">
        <div className="grid gap-8 md:grid-cols-2">
          <img
            src={`${product.image}`}
            alt={product.name}
            className="h-full max-h-[480px] w-full rounded-2xl object-cover"
          />
          <div className="flex-1">
            <p className="text-xs font-semibold uppercase tracking-[0.18em] text-orange-700">Featured</p>
            <h1 className="mt-2 text-4xl font-bold text-stone-900">
              {product.name}
            </h1>
            <p className="mb-5 mt-4 leading-relaxed text-stone-600">{product.description || "A premium pick crafted for your everyday experience."}</p>
            <p className="mb-7 text-3xl font-bold text-orange-700">
              ${product.price}
            </p>
            <button onClick={handleAddToCart} className="rounded-xl bg-stone-900 px-6 py-3 text-sm font-semibold text-white transition hover:bg-black md:text-base">
                Add to cart
            </button>
            <div className="mt-5">
              <Link to="/" className="text-sm font-semibold text-orange-700 hover:underline">
                &larr; Continue browsing
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProductDetails;