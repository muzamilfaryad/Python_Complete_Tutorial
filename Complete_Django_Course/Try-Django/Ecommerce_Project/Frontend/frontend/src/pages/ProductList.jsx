import { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard.jsx";

function ProductList() {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const BASEURL = import.meta.env.VITE_DJANGO_BASE_URL;

    useEffect(() => {
        fetch(`${BASEURL}/api/products/`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to fetch products");
            }
            return response.json();
        })
        .then((data)=>{
            setProducts(data);
            setLoading(false);
        })
        .catch((error)=>{
            setError(error.message);
            setLoading(false);
        });
    }, []);

    if (loading) {
        return <div className="pt-32 text-center text-stone-700">Loading our latest collection...</div>;
    }

    if (error) {
        return <div className="pt-32 text-center text-red-700">We could not load products right now: {error}</div>;
    }

    return (
        <div className="min-h-screen px-5 pb-10 pt-24 md:px-8">
            <section className="mx-auto mb-8 max-w-7xl rounded-3xl border border-orange-100 bg-white/80 p-7 shadow-sm backdrop-blur-sm md:p-10">
                <p className="mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-orange-700">Fresh arrivals</p>
                <h1 className="text-4xl font-bold text-stone-900 md:text-5xl">Find products worth showing off.</h1>
                <p className="mt-4 max-w-2xl text-sm text-stone-600 md:text-base">
                    Explore a handpicked storefront with clean design, smooth browsing, and standout essentials for your next upgrade.
                </p>
            </section>
            <div className="mx-auto grid max-w-7xl grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
                {products.length > 0 ? (
                    products.map((product) => (
                        <ProductCard key={product.id} product={product} />
                    ))
                ) : (
                    <p className="col-span-full rounded-2xl border border-dashed border-orange-200 bg-white/80 p-8 text-center text-stone-500">
                        No products are available right now. Please check back in a few minutes.
                    </p>
                )}
            </div>
        </div>
    )
}

export default ProductList;