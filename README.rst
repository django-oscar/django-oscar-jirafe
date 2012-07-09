============================
Jirafe integration for Oscar
============================

This is an extension for `django-oscar`_ that makes integration with the
`Jirafe`_ e-commerce tracking easy.

.. _`django-oscar`: http://oscarcommerce.com
.. _`Jirafe`: http://jirafe.com/

Installation
------------

Install from Github (not on PyPi yet)::

    pip install git+git://github.com/tangentlabs/django-oscar-jirafe.git#egg=django-oscar-jirafe

Now add ``jirafe`` to your ``INSTALLED_APPS`` and update your
``TEMPLATE_CONTEXT_PROCESSORS`` to include ``jirafe.context_processors.jirafe``.
Also, set ``JIRAFE_ID`` to be your Jirafe ID.

Finally, you need to include the tracking javascript in your templates.  You can
do this by including::

    {% include 'jirafe/tracking.html' %} 

within your ``base.html`` template.  An example ``base.html`` is included which
you can copy into place to get you started.

That's it - the stats should start appearing in your Jirafe dashboard.
