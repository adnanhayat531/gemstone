
content = """{% extends 'base.html' %}

{% block content %}
<div class="bg-light py-5">
    <div class="container">
        <h1 class="text-center fw-bold display-4 mb-3">Our Collection</h1>
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb justify-content-center">
                <li class="breadcrumb-item"><a href="{% url 'home' %}" class="text-decoration-none text-gold">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Collection</li>
            </ol>
        </nav>
    </div>
</div>

<div class="container py-5">
    <div class="row">
        <!-- Sidebar Filters -->
        <div class="col-lg-3 mb-4">
            <div class="card border-0 shadow-sm p-3">
                <h5 class="fw-bold mb-4">Filter By</h5>
                
                <form action="{% url 'gemstone_list' %}" method="get">
                    <div class="mb-3">
                        <label class="form-label fw-bold small">Category</label>
                        <select name="category" class="form-select form-select-sm" onchange="this.form.submit()">
                            <option value="">All Categories</option>
                            <option value="Ruby" {% if request.GET.category == 'Ruby' %}selected{% endif %}>Ruby</option>
                            <option value="Sapphire" {% if request.GET.category == 'Sapphire' %}selected{% endif %}>Sapphire</option>
                            <option value="Emerald" {% if request.GET.category == 'Emerald' %}selected{% endif %}>Emerald</option>
                            <option value="Diamond" {% if request.GET.category == 'Diamond' %}selected{% endif %}>Diamond</option>
                            <option value="Amethyst" {% if request.GET.category == 'Amethyst' %}selected{% endif %}>Amethyst</option>
                            <option value="Other" {% if request.GET.category == 'Other' %}selected{% endif %}>Other</option>
                        </select>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label fw-bold small">Sort By</label>
                        <select name="sort" class="form-select form-select-sm" onchange="this.form.submit()">
                            <option value="newest" {% if request.GET.sort == 'newest' %}selected{% endif %}>Newest Arrivals</option>
                            <option value="price_asc" {% if request.GET.sort == 'price_asc' %}selected{% endif %}>Price: Low to High</option>
                            <option value="price_desc" {% if request.GET.sort == 'price_desc' %}selected{% endif %}>Price: High to Low</option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label class="form-label fw-bold small">Origin</label>
                         <input type="text" name="origin" class="form-control form-control-sm" placeholder="e.g. Burma" value="{{ request.GET.origin|default:'' }}">
                    </div>

                    <button type="submit" class="btn btn-gold btn-sm w-100 mb-2">Apply Filters</button>
                    <a href="{% url 'gemstone_list' %}" class="btn btn-outline-secondary btn-sm w-100">Clear All</a>
                </form>
            </div>
        </div>

        <!-- Gemstone Grid -->
        <div class="col-lg-9">
            <div class="row">
                {% for gemstone in gemstones %}
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card card-gemstone h-100 shadow-sm">
                        <div class="card-img-top-wrapper">
                            {% if gemstone.image %}
                            <img src="{{ gemstone.image.url }}" class="card-img-top" alt="{{ gemstone.name }}">
                            {% else %}
                            <div class="d-flex align-items-center justify-content-center h-100 bg-light text-muted">
                                No Image
                            </div>
                            {% endif %}
                        </div>
                        <div class="card-body text-center">
                            <h5 class="card-title fw-bold font-serif">{{ gemstone.name }}</h5>
                            <p class="card-text text-muted mb-1">{{ gemstone.carat }} Carat {{ gemstone.category }}</p>
                            <h5 class="text-gold fw-bold mb-3">${{ gemstone.price }}</h5>
                            <a href="{% url 'gemstone_detail' gemstone.slug %}" class="btn btn-outline-gold rounded-pill px-4">View Details</a>
                        </div>
                    </div>
                </div>
                {% empty %}
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">No gemstones found matching your criteria.</h4>
                    <a href="{% url 'gemstone_list' %}" class="btn btn-outline-gold mt-3">Browse All</a>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

with open(r"c:\Users\adnan.h\Desktop\projects\gemstone\templates\store\gemstone_list.html", "w", encoding="utf-8") as f:
    f.write(content)

print("File overwritten successfully.")
