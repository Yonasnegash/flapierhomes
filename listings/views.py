from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, bathroom_choices, city_choices, sqft_choices
from .models import Listing
from hometype.models import HomeType

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'city_choices': city_choices,
        'sqft_choices': sqft_choices,
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    recent_listins = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listing': listing,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'city_choices': city_choices,
        'sqft_choices': sqft_choices,
        'recent_listings': recent_listins,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Sqft
    if 'sqft' in request.GET:
        sqft = request.GET['sqft']
        if sqft:
            queryset_list = queryset_list.filter(sqft__lte=sqft)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'city_choices': city_choices,
        'sqft_choices': sqft_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)