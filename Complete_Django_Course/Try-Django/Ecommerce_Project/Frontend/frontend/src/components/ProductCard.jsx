import { Link } from "react-router-dom";

function ProductCard({ product }) {
  const BASEURL = import.meta.env.VITE_DJANGO_BASE_URL;
  return (
    <Link to={`/product/${product.id}`}>
      <div className="group h-full cursor-pointer rounded-2xl border border-orange-100 bg-white/90 p-4 shadow-sm transition duration-300 hover:-translate-y-1 hover:border-orange-300 hover:shadow-xl">
        <img
          src={`${BASEURL}${product.image}`}
          alt={product.name}
          className="mb-4 h-56 w-full rounded-xl object-cover"
        />
        <p className="mb-2 text-xs font-semibold uppercase tracking-[0.16em] text-orange-700">
          Curated Pick
        </p>
        <h2 className="truncate text-lg font-semibold text-stone-900">
          {product.name}
        </h2>
        <div className="mt-3 flex items-center justify-between">
          <p className="font-bold text-stone-800">${product.price}</p>
          <p className="text-sm font-medium text-orange-700 transition group-hover:translate-x-1">
            View details &rarr;
          </p>
        </div>
      </div>
    </Link>
  );
}

export default ProductCard;