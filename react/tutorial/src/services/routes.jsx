import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { Page1 } from '../pages/page1';

export const RoutesService = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/page1" element={<Page1 />} />
            </Routes>
        </BrowserRouter>
    )
}
